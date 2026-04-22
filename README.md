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

 1. Adım: Klonlama ve Kurulum

git clone https://github.com/<KULLANICI_ADIN>/LifeGuard-AI.git
cd LifeGuard-AI
pip install -r requirements.txt

 2. Adım: Yapılandırma (.env)
Proje dizininde .env adında bir dosya oluşturun ve şu bilgileri ekleyin:

Kod snippet'i
TELEGRAM_TOKEN=sizin_bot_tokeniniz
TELEGRAM_CHAT_ID=sizin_chat_idniz
CAMERA_SOURCE=0

 3. Adım: Çalıştırma
Projeyi yerel ortamda çalıştırmak için:

Bash
python proje.py

4. Adım: Docker ile Çalıştırma (Cloud Ready)
Sistemi herhangi bir sunucuda veya konteyner içinde çalıştırmak için:

Bash
docker build -t lifeguard-ai .
docker run -p 5000:5000 lifeguard-ai

Geliştirici: Enes Çelik
