# LifeGuard AI 🛡️

LifeGuard AI, postür analizi ve yapay zeka tabanlı güvenlik takibi için geliştirilmiş ölçeklenebilir bir sistemdir.

## 📌 Proje Hakkında
LifeGuard AI, günümüz güvenlik ihtiyaçlarına modern çözümler sunan, hem yerel hem de bulut tabanlı çalışabilen bir yapay zeka sistemidir.

## 🎯 Mevcut Durum (MVP)
Sistem şu an şu özellikleri barındırır:
- **Anlık Postür Analizi**: Kullanıcının duruşunu gerçek zamanlı izler.
- **Acil Durum Tespiti**: Bayılma, uyku veya sağlık sorunlarını analiz eder.
- **Telegram Entegrasyonu**: İhlal anında delil (fotoğraf/video) göndererek anında uyarı sağlar.
- **Esnek Kamera Desteği**: Hem yerel (Webcam) hem de IP Kamera (RTSP) desteği ile evrensel izleme.

## 🌐 Gelecek Vizyonu
Sistem, yerel bir takip aracından çıkarak; bulut (cloud) altyapısı ve çoklu ortam denetimi ile evrensel bir güvenlik platformuna dönüşmektedir:
- **Bulut Hazır (Cloud-Ready)**: Docker altyapısı sayesinde herhangi bir sunucuda 7/24 çalışabilir.
- **Genişletilmiş Güvenlik**: Yabancı kişi tespiti, duman/yangın algılama modülleri.

## 🚀 Teknik Mimari
- **Core AI**: MediaPipe (Pose Landmark Detection)
- **Containerization**: Docker (Dağıtılabilir altyapı)
- **Web Server**: Flask
- **Backend**: Python, Threading
- **Network**: REST API (Telegram Bot API)

## 🛠️ Kurulum

### 1. Yerel Kurulum
Terminalde projenin olduğu klasöre giderek kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
