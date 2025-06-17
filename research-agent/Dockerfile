FROM python:3.11-slim

# uv'yi ekleyelim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Bağımlılık dosyaları
COPY pyproject.toml uv.lock ./

# Bağımlılıkları uv ile kur
RUN uv sync --locked

# Uygulama dosyalarını kopyala
COPY . .

# Uygulama başlatma
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]