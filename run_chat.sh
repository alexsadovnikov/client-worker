#!/bin/bash

echo "➡️ Переход в папку clientservice/chat..."
cd ./clientservice/chat/ || { echo "❌ Не удалось перейти в папку"; exit 1; }

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Запуск WebSocket chat-сервера на порту 5052..."
python3 app/main.py