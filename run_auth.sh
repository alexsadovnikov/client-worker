#!/bin/bash

echo "➡️ Переход в папку clientservice/auth..."
cd ./clientservice/auth/ || { echo "❌ Не удалось перейти в папку"; exit 1; }

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Устанавливаю FLASK_APP..."
export FLASK_APP=app.main:create_app

echo "➡️ Запуск auth-сервиса на порту 5051..."
flask run --host=0.0.0.0 --port=5051