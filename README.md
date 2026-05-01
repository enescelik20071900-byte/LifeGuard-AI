# 🛡️ LifeGuard AI

**LifeGuard AI**, MediaPipe Pose Detection teknolojisiyle insan postürünü gerçek zamanlı analiz eden ve yerel ağdaki kamera görüntülerini buluta güvenli şekilde aktarabilen hibrit bir yapay zeka güvenlik sistemidir.

---

## 📌 Proje Hakkında

LifeGuard AI, geleneksel güvenlik sistemlerinden farklı olarak yalnızca görüntü kaydı yapmakla kalmaz; görüntüdeki insan hareketlerini matematiksel olarak analiz eder.

MediaPipe Pose Detection kullanarak insan vücudundaki **33 farklı eklem noktasını (landmarks)** takip eder ve bu veriler üzerinden anlamlı çıkarımlar yapar.

### 🎯 Tespit Edilen Durumlar

* 🚨 **Bayılma / Düşme Tespiti**
  Omuz çizgisinin belirli bir eşik değerin altına düşmesi

* 😴 **Uyku / Hareketsizlik Tespiti**
  Uzun süreli hareketsizlik + baş pozisyonu analizi

* 🚶 **Duruş & Alan Takibi**
  Belirlenen güvenli alan dışına çıkış

---

## 🚀 Geliştirme Yol Haritası (Roadmap)

### ✅ Tamamlananlar

* MediaPipe Pose Detection entegrasyonu
* Ngrok ile yerel kamerayı internete açma
* Hugging Face Spaces ile cloud deployment
* SQLite ile olay kayıt sistemi

### 🔄 Devam Edenler

* Çoklu kamera (multi-stream) desteği
* React tabanlı admin dashboard paneli

---

## 🎯 Mevcut Özellikler

### 📡 Ngrok & Bulut Entegrasyonu

Yerel ağdaki IP kamera (telefon/webcam) görüntüsünü güvenli bir tünel üzerinden buluta aktarma.

### 🚨 Akıllı Analiz & Bildirim

33 noktalı insan iskelet modeli üzerinden anlık analiz ve anomali durumunda olay tetikleme sistemi.

### 🐳 Containerized Architecture

Docker ve Hugging Face container altyapısı sayesinde hızlı ve taşınabilir kurulum.

---

## 🛠️ Teknik Mimari

| Katman     | Teknoloji                       |
| ---------- | ------------------------------- |
| Core AI    | MediaPipe (Pose Landmark Lite)  |
| Backend    | Python 3.9, Flask, Threading    |
| Tünelleme  | Ngrok (Reverse Proxy)           |
| Cloud      | Hugging Face Spaces (Container) |
| Veritabanı | SQLite                          |

---

## ⚙️ Kurulum ve Çalıştırma

### 1️⃣ Projeyi Klonla

```bash
git clone https://github.com/enescelik20071900-byte/LifeGuard-AI.git
cd LifeGuard-AI
pip install -r requirements.txt
```

---

### 2️⃣ Kamera Bağlantısı (Remote Camera)

Eğer kameranız yerel ağdaysa (örneğin telefon IP Webcam), ngrok ile tünel başlatın:

```bash
ngrok http [KAMERA_IP]:[PORT]
```

---

### 3️⃣ Kamera Kaynağını Ayarla

`.env` dosyasında veya `proje.py` içinde:

```python
CAMERA_SOURCE = "https://xxxx.ngrok-free.dev/video"
```

---

## 👨‍💻 Geliştirici

**Enes Çelik**
Bursa Uludağ Üniversitesi
Bilgisayar Mühendisliği

---

Projeyi beğendiysen ⭐ bırakmayı unutma!
Geliştirmeye katkı sağlamak için pull request gönderebilirsin.
