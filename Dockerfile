FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Ставим зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Кладём весь проект внутрь контейнера
COPY . .

# ВРЕМЕННАЯ команда, чтобы контейнер просто жил и не падал
# Потом сюда поставим реальный запуск (python ... или uvicorn ...)
CMD ["tail", "-f", "/dev/null"]