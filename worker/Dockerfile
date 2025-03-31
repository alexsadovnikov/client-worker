FROM python:3.10-slim

# Создание рабочей директории
WORKDIR /app

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Запуск приложения
CMD ["python", "worker.py"]
