import os
import cv2
import mediapipe as mp
import time
import winsound
import math
import sqlite3
import requests
import threading
from datetime import datetime
from collections import deque
from flask import Flask, render_template_string, Response, jsonify

# --- AYARLAR ---
TELEGRAM_TOKEN = "8606813928:AAG-mugYrEUfMRh7Rnmbder6yAKjI-CKaDw"
TELEGRAM_CHAT_ID = "8280019169"
KAFA_ACI_ESIGI = 40 
OMUZ_ESIGI = 8         
CAMERA_SOURCE = "http://10.166.106.89:8080/video" # IP Webcam adresin

# --- THREADED CAMERA CLASS (Kasma Önleyici) ---
class CameraStream:
    def __init__(self, src):
        self.cap = cv2.VideoCapture(src)
        self.frame = None
        self.lock = threading.Lock()
        self.running = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self.lock:
                    self.frame = frame
            time.sleep(0.01)

    def read(self):
        with self.lock:
            return self.frame

    def stop(self):
        self.running = False
        self.cap.release()

# --- VERİTABANI ---
def init_db():
    conn = sqlite3.connect('lifeguard_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, user TEXT, status TEXT, details TEXT)''')
    conn.commit()
    conn.close()

def log_to_db(user, status, details):
    try:
        conn = sqlite3.connect('lifeguard_logs.db')
        c = conn.cursor()
        c.execute("INSERT INTO logs (timestamp, user, status, details) VALUES (?, ?, ?, ?)",
                  (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user, status, details))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Veritabanı hatası: {e}")

# --- ARKA PLAN GÖNDERİM ---
def background_evidence_task(photo_frame, video_frames, message):
    try:
        photo_name = "evidence.jpg"
        video_name = "evidence.mp4"
        cv2.imwrite(photo_name, photo_frame)
        
        h, w, _ = photo_frame.shape
        fourcc = cv2.VideoWriter_fourcc(*'avc1') 
        out = cv2.VideoWriter(video_name, fourcc, 20.0, (w, h))
        for f in video_frames: out.write(f)
        out.release()
        
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={"chat_id": TELEGRAM_CHAT_ID, "text": message})
        with open(photo_name, "rb") as p: requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto", files={"photo": p}, data={"chat_id": TELEGRAM_CHAT_ID})
        with open(video_name, "rb") as v: requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo", files={"video": v}, data={"chat_id": TELEGRAM_CHAT_ID})
    except Exception as e:
        print(f"Gönderim hatası: {e}")

# --- BAŞLATMALAR ---
init_db()
stream = CameraStream(CAMERA_SOURCE)
app = Flask(__name__)
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=0)

video_buffer = deque(maxlen=100) 
angle_history = deque(maxlen=15) 
start_time = 0
is_suspicious = is_logged = False
progress_bar = 0
frame_counter = 0

def generate_frames():
    global start_time, is_suspicious, is_logged, progress_bar, frame_counter
    
    last_results = None
    
    while True:
        frame = stream.read()
        
        if frame is None:
            time.sleep(0.1)
            continue
            
        video_buffer.append(frame.copy())
        frame_counter += 1
        now_ts = time.time()
        
        frame_small = cv2.resize(frame, (640, 480))
        avg_angle = 0
        s_tilt = 0

        # AI Analizi
        if frame_counter % 3 == 0:
            rgb_frame = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)
            last_results = pose.process(rgb_frame)
            
        if last_results and last_results.pose_landmarks:
            lm = last_results.pose_landmarks.landmark
            if lm[0].visibility > 0.5:
                mp_drawing.draw_landmarks(frame, last_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                
                dx = abs(lm[0].x - (lm[11].x + lm[12].x)/2)
                dy = abs(lm[0].y - (lm[11].y + lm[12].y)/2)
                k_angle = math.degrees(math.atan2(dy, dx)) if dx != 0 else 90
                angle_history.append(k_angle)
                avg_angle = sum(angle_history) / len(angle_history)
                s_tilt = abs(lm[11].y - lm[12].y) * 100 

                if avg_angle < KAFA_ACI_ESIGI:
                    if not is_suspicious: start_time = now_ts
                    is_suspicious = True
                    elapsed = now_ts - start_time
                    progress_bar = min(int((elapsed / 5) * 100), 100)
                    
                    if elapsed >= 5 and not is_logged:
                        status = "BAYILMA" if s_tilt > OMUZ_ESIGI else "UYKU MODU"
                        detay = f"Kafa Acisi: {int(avg_angle)}° | Omuz Acisi: {int(s_tilt)}°"
                        log_to_db("ENES CELIK", status, detay)
                        
                        msg = f"⚠️ TEHLIKE! {status}\nUser: ENES CELIK\n{detay}\nSaat: {datetime.now().strftime('%H:%M:%S')}"
                        threading.Thread(target=background_evidence_task, args=(frame.copy(), list(video_buffer), msg)).start()
                        winsound.Beep(1000, 500)
                        is_logged = True
                else:
                    is_suspicious = is_logged = False
                    start_time = progress_bar = 0
            else:
                is_suspicious = is_logged = False
        else:
            is_suspicious = is_logged = False
            start_time = progress_bar = 0

        # HUD ÇİZİMİ
        cv2.rectangle(frame, (10, 10), (450, 180), (0,0,0), -1) 
        st = datetime.now().strftime('%H:%M:%S')
        clr = (0, 0, 255) if is_logged else ((0, 165, 255) if is_suspicious else (0, 255, 0))
        
        cv2.putText(frame, f"SAAT: {st}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.putText(frame, f"DURUM: {'TEHLIKE' if is_suspicious else 'OK'}", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, clr, 2)
        cv2.putText(frame, f"Kafa Acisi: {int(avg_angle)} | Omuz Acisi: {int(s_tilt)}", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        if is_suspicious:
            cv2.rectangle(frame, (20, 160), (360, 170), (255, 255, 255), 1)
            cv2.rectangle(frame, (21, 161), (21 + int(progress_bar*3.38), 169), (0, 165, 255), -1)

        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# --- WEB PANEL ROUTE ---
@app.route('/')
def index():
    return render_template_string('''
        <html><head><title>LifeGuard AI</title><style>
            body { background: #0f0f0f; color: white; font-family: sans-serif; text-align: center; }
            .v-box { margin: 20px auto; width: 80%; max-width: 800px; border: 3px solid #00aaff; border-radius: 15px; overflow: hidden; }
            img { width: 100%; }
            .btn { padding: 15px 35px; background: #00aaff; color: white; border: none; border-radius: 30px; cursor: pointer; font-weight: bold; }
        </style></head>
        <body>
            <h1 style="color: #00aaff;">🛡️ LIFEGUARD AI MONITOR</h1>
            <div class="v-box"><img src="/video_feed"></div>
            <a href="/archive"><button class="btn">📊 OLAY ARŞİVİNİ GÖRÜNTÜLE</button></a>
        </body></html>
    ''')

@app.route('/archive')
def archive():
    return render_template_string('''
        <html><head><title>Arşiv</title><style>
            body { background: #0f0f0f; color: white; font-family: sans-serif; text-align: center; padding: 20px; }
            table { width: 90%; margin: 20px auto; border-collapse: collapse; background: #1a1a1a; }
            th, td { padding: 12px; border: 1px solid #333; }
            th { background: #00aaff; color: black; }
        </style></head>
        <body>
            <h1>OLAY GEÇMİŞİ</h1>
            <a href="/" style="color: #00aaff; font-size: 20px; text-decoration: none;">⬅ GERİ DÖN</a>
            <table>
                <thead><tr><th>ZAMAN</th><th>DURUM</th><th>ANALİZ (AÇILAR)</th></tr></thead>
                <tbody id="logBody"></tbody>
            </table>
            <script>
                fetch('/get_logs').then(r => r.json()).then(data => {
                    const b = document.getElementById("logBody");
                    data.forEach(l => { b.innerHTML += `<tr><td>${l[1]}</td><td>${l[3]}</td><td>${l[4]}</td></tr>`; });
                });
            </script>
        </body></html>
    ''')

@app.route('/get_logs')
def get_logs():
    conn = sqlite3.connect('lifeguard_logs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY id DESC")
    res = c.fetchall()
    conn.close()
    return jsonify(res)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    except KeyboardInterrupt:
        stream.stop()
