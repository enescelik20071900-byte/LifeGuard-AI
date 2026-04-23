FROM python:3.9-slim

# Sistem kütüphanelerini güncelle (OpenCV için şart)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Cache'i zorla temizle ve paketleri kur
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Çalıştır
CMD ["python", "proje.py"]
