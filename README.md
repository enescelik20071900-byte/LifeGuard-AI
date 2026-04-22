# LifeGuard AI 🛡️

LifeGuard AI, postür analizi ve yapay zeka tabanlı güvenlik takibi için geliştirilmiş ölçeklenebilir bir sistemdir.

## 📌 Proje Hakkında

### 🎯 Mevcut Durum (MVP)
Şu anki aşamada sistem, kişisel bilgisayar (localhost) ortamında;
- Bilgisayar başındaki kullanıcının postürünü (duruşunu) anlık analiz eder.
- Bayılma, uyku veya sağlık sorunları gibi acil durumları tespit eder.
- Telegram üzerinden fotoğraf ve video delil göndererek anında uyarı sağlar.

### 🌐 Gelecek Vizyonu
LifeGuard AI, yerel bir postür takip aracından çıkarak; **IP kamera desteği, bulut (cloud) altyapısı ve çoklu ortam denetimi** ile evrensel bir güvenlik platformuna dönüştürülmektedir. 
- **Her Yerde Güvenlik:** Sadece bilgisayar başı değil; ev, ofis, fabrika veya kamu alanlarında 7/24 izleme.
- **Evrensel İzleme:** IP kameralar üzerinden dünyanın her yerinden sisteme bağlanabilme.
- **Geniş Kapsamlı Analiz:** Sadece postür değil; yabancı kişi tespiti, duman/yangın algılama ve anormal hareket takibi gibi genişletilmiş güvenlik modülleri.

## 🚀 Teknik Mimari
- **Core AI:** MediaPipe (Pose Landmark Detection)
- **Web Server:** Flask
- **Backend:** Python, Threading (Arka plan görevleri)
- **Database:** SQLite
- **Network:** REST API (Telegram Bot API)

## 🛠️ Kurulum

### 1. Gereksinimler
Terminalde projenin olduğu klasöre giderek kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
