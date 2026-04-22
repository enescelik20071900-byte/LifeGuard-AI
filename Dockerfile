FROM python:3.9-slim

# Sunucuya gerekli kütüphaneleri (OpenCV için) yüklüyoruz
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "proje.py"]
