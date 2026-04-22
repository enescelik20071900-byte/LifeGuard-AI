FROM python:3.9-slim

# libx264-dev ekledik, video encode işlemleri için şart!
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libx264-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "proje.py"]
