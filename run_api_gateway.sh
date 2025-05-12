#!/bin/bash

echo "➡️ Переход в папку clientservice/api_gateway..."
cd ./clientservice/api_gateway/ || { echo "❌ Не удалось перейти в папку"; exit 1; }

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Устанавливаю переменную среды FLASK_APP..."
export FLASK_APP=app.main:app

echo "➡️ Проверяю наличие файла swagger-ui.html..."
if [ ! -f app/static/swagger-ui.html ]; then
  echo "❌ Файл swagger-ui.html не найден. Остановка."
  exit 1
fi

echo "➡️ Запуск Flask-приложения на порту 5069..."
flask run --host=0.0.0.0 --port=5069