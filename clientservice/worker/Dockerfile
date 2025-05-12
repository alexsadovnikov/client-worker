FROM python:3.10-slim
ENV PYTHONPATH=/app/shared
WORKDIR /app

# Сначала ставим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Затем копируем весь код
COPY . .

# И запускаем основной скрипт
CMD ["python", "worker.py"]
