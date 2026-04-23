FROM python:3.9-slim

# Gerekli sistem kütüphaneleri
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libx264-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Tüm dosyaları kopyala
COPY . .

# Kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı başlat
CMD ["python", "proje.py"]
