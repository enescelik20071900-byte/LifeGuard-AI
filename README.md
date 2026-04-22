# LifeGuard AI 🛡️

LifeGuard AI, postür analizi ve yapay zeka tabanlı güvenlik takibi için geliştirilmiş, ölçeklenebilir ve modüler bir sistemdir.

## 📌 Proje Hakkında
LifeGuard AI, günümüz güvenlik ihtiyaçlarına modern çözümler sunan, hem yerel hem de bulut tabanlı çalışabilen bir yapay zeka sistemidir. Sistem, insan postürünü gerçek zamanlı analiz ederek olası sağlık sorunlarını veya güvenlik ihlallerini tespit eder.



## 🚀 Geliştirme Yol Haritası (Roadmap)

* **[TAMAMLANDI]** Core AI (MediaPipe Pose Detection) entegrasyonu.
* **[TAMAMLANDI]** Telegram Bot API ile anlık bildirim sistemi.
* **[TAMAMLANDI]** Docker container yapısı ile yerel kurulum altyapısı.
* **[DEVAM EDİYOR]** IP Kamera (RTSP/Stream) desteği ve optimizasyonu.
* **[DEVAM EDİYOR]** Bulut (Cloud) deploy süreçleri (Render/AWS/GCP).
* **[PLANLANIYOR]** Çoklu kamera desteği ve dashboard paneli.

## 🎯 Mevcut Özellikler
* **Anlık Postür Analizi**: Kullanıcının duruşunu gerçek zamanlı izler ve açısal analiz yapar.
* **Acil Durum Tespiti**: Bayılma, uyku modu veya hareketsizlik durumlarını algılar.
* **Telegram Entegrasyonu**: İhlal anında delil (fotoğraf ve video) göndererek kullanıcıyı bilgilendirir.
* **Containerized Architecture**: Docker sayesinde her türlü ortamda izole ve hızlı çalışma.

## 🛠️ Teknik Mimari
* **Core AI**: MediaPipe (Pose Landmark Detection)
* **Backend**: Python, Flask, Threading (Asenkron işlemler)
* **Database**: SQLite (Olay günlüğü ve analiz verileri)
* **Network**: REST API (Telegram Bot)

## ⚙️ Kurulum ve Gereksinimler

Proje **Python 3.9+** sürümü ile geliştirilmiştir. Bağımlılıklar `requirements.txt` dosyasında tanımlanmıştır.

### 1. Gerekli Kütüphaneler
Projenin ihtiyaç duyduğu ana kütüphaneler şunlardır:
* `flask`: Web arayüzü ve sunucu yönetimi.
* `mediapipe`: Postür tespiti ve AI model motoru.
* `opencv-python-headless`: Görüntü işleme (Headless sürüm sunucu optimizasyonu içindir).
* `requests`: Telegram bot API ile haberleşme.
* `python-dotenv`: `.env` dosyası üzerinden güvenli konfigürasyon yönetimi.

### 2. Adım Adım Kurulum
1. **Repoyu Klonlayın:**
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/LifeGuard-AI.git](https://github.com/KULLANICI_ADIN/LifeGuard-AI.git)
   cd LifeGuard-AI
