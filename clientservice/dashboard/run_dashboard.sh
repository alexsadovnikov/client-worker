#!/bin/bash

echo "➡️ Переход в папку dashboard..."
cd "$(dirname "$0")" || exit 1

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Проверяю порт 8501..."
PORT=8501
PID=$(lsof -ti tcp:$PORT)
if [ ! -z "$PID" ]; then
  echo "⚠️ Найден процесс на порту $PORT (PID=$PID), убиваю его..."
  kill -9 $PID
fi

echo "✅ Запуск Streamlit-дэшборда..."
streamlit run streamlit_app.py --server.port $PORT --server.headless true