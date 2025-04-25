# services/worker/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 1) Устанавливаем зависимости
COPY services/worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Копируем код самого воркера
COPY services/worker/app   ./app
COPY services/worker/worker.py .

# 3) Копируем pydantic-схемы в /app/schemas
COPY shared/schemas       ./schemas

CMD ["python", "worker.py"]
