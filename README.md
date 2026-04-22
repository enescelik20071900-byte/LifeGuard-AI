# 🛡️ LifeGuard AI

**LifeGuard AI**, postür analizi ve yapay zeka tabanlı güvenlik takibi için geliştirilmiş, ölçeklenebilir ve modüler bir sistemdir.

---

## 📌 Proje Hakkında

LifeGuard AI, günümüz güvenlik ihtiyaçlarına modern çözümler sunan; hem **yerel (local)** hem de **bulut (cloud)** ortamlarında çalışabilen bir yapay zeka sistemidir.

Sistem, **MediaPipe Pose Detection** teknolojisini kullanarak insan postürünü gerçek zamanlı analiz eder ve:

* Bayılma
* Uyku hali
* Duruş bozukluğu

gibi durumları tespit ederek anında bildirim gönderir.

---

## 🚀 Geliştirme Yol Haritası (Roadmap)

* ✅ Core AI (MediaPipe Pose Detection) entegrasyonu
* ✅ Telegram Bot API ile anlık bildirim sistemi
* ✅ Docker container altyapısı
* 🔄 IP Kamera (RTSP/Stream) desteği ve optimizasyonu
* 🔄 Bulut (Cloud/Render) deploy süreçleri
* 🧠 Çoklu kamera desteği
* 📊 Yönetici dashboard paneli

---

## 🎯 Mevcut Özellikler

* **📡 Anlık Postür Analizi**
  Gerçek zamanlı duruş takibi ve açısal analiz

* **🚨 Acil Durum Tespiti**
  Bayılma, uyku veya hareketsizlik algılama

* **📲 Telegram Entegrasyonu**
  Olay anında fotoğraf ve video ile bildirim

* **🐳 Containerized Architecture**
  Docker ile hızlı, taşınabilir ve izole çalışma

---

## 🛠️ Teknik Mimari

| Katman   | Teknoloji                  |
| -------- | -------------------------- |
| Core AI  | MediaPipe (Pose Detection) |
| Backend  | Python, Flask, Threading   |
| Database | SQLite                     |
| Network  | REST API, Telegram Bot API |

---

## ⚙️ Kurulum ve Gereksinimler

Proje **Python 3.9+** ile geliştirilmiştir.

### 🔧 Kurulum

```bash
git clone https://github.com/enescelik20071900-byte/LifeGuard-AI.git
cd LifeGuard-AI
pip install -r requirements.txt
```

### 🔑 .env Ayarları

```env
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
CAMERA_SOURCE=0
```

### ▶️ Çalıştırma

```bash
python proje.py
```

### 🐳 Docker

```bash
docker build -t lifeguard-ai .
docker run -p 5000:5000 lifeguard-ai
```

---

## 👨‍💻 Geliştirici

**Enes Çelik**
