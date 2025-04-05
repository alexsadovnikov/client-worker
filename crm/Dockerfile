FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из папки crm в рабочую директорию
COPY . .

# Устанавливаем зависимости (только Flask)
RUN pip install --no-cache-dir flask

# Указываем команду запуска
CMD ["python", "crm_mock.py"]
