FROM python:3.9-slim

# Gerekli sistem kütüphanelerini artırıyoruz (mediapipe/opencv için kritik)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Cache'i tamamen devre dışı bırakıp zorla güncel kurulum yaptır
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 7860
CMD ["python", "proje.py"]
