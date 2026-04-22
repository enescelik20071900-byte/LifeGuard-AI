# LifeGuard AI 🛡️

LifeGuard AI, postür analizi ve yapay zeka tabanlı güvenlik takibi için geliştirilmiş, ölçeklenebilir ve modüler bir sistemdir.

## 📌 Proje Hakkında
LifeGuard AI, günümüz güvenlik ihtiyaçlarına modern çözümler sunan, hem yerel hem de bulut tabanlı çalışabilen bir yapay zeka sistemidir. Sistem, MediaPipe teknolojisini kullanarak insan postürünü gerçek zamanlı analiz eder ve olası sağlık sorunlarını (bayılma, uyku modu, duruş bozukluğu) tespit ederek anında bildirim gönderir.

## 🚀 Geliştirme Yol Haritası (Roadmap)

- **[TAMAMLANDI]** Core AI (MediaPipe Pose Detection) entegrasyonu.
- **[TAMAMLANDI]** Telegram Bot API ile anlık görsel/video bildirim sistemi.
- **[TAMAMLANDI]** Docker container yapısı ile yerel kurulum altyapısı.
- **[DEVAM EDİYOR]** IP Kamera (RTSP/Stream) desteği ve optimizasyonu.
- **[DEVAM EDİYOR]** Bulut (Cloud/Render) deploy süreçleri.
- **[PLANLANIYOR]** Çoklu kamera desteği ve yönetici dashboard paneli.

## 🎯 Mevcut Özellikler
* **Anlık Postür Analizi**: Kullanıcının duruşunu gerçek zamanlı izler ve açısal analiz yapar.
* **Acil Durum Tespiti**: Bayılma, uyku modu veya hareketsizlik durumlarını otomatik algılar.
* **Telegram Entegrasyonu**: İhlal anında delil (fotoğraf ve video) göndererek anında uyarı sağlar.
* **Containerized Architecture**: Docker sayesinde her türlü ortamda izole ve hızlı çalışma garantisi.

## 🛠️ Teknik Mimari
* **Core AI**: MediaPipe (Pose Landmark Detection)
* **Backend**: Python, Flask, Threading (Asenkron işlemler)
* **Database**: SQLite (Olay günlüğü ve analiz verileri)
* **Network**: REST API (Telegram Bot API)

## ⚙️ Kurulum ve Gereksinimler

Proje **Python 3.9+** sürümü ile geliştirilmiştir. Bağımlılıklar `requirements.txt` dosyasında tanımlanmıştır.

### 1. Adım: Klonlama ve Kurulum
```bashTELEGRAM_TOKEN=sizin_bot_tokeniniz
TELEGRAM_CHAT_ID=sizin_chat_idniz
CAMERA_SOURCE=0python proje.pydocker build -t lifeguard-ai .
docker run -p 5000:5000 lifeguard-ai
git clone [https://github.com/enescelik20071900-byte/LifeGuard-AI.git](https://github.com/enescelik20071900-byte/LifeGuard-AI.git)
cd LifeGuard-AI
pip install -r requirements.txt
