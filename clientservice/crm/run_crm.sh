#!/bin/bash

echo "➡️ Переход в папку crm..."
cd "$(dirname "$0")" || exit 1

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Устанавливаю переменные среды..."
export FLASK_APP=app:create_app
PORT=5053

echo "➡️ Проверяю порт $PORT..."
PID=$(lsof -ti tcp:$PORT)
if [ ! -z "$PID" ]; then
  echo "⚠️ Найден процесс на порту $PORT (PID=$PID), убиваю его..."
  kill -9 $PID
fi

echo "➡️ Проверка наличия каталога миграций Alembic..."
if [ ! -d "migrations" ]; then
  echo "🛠️  Каталог migrations не найден, инициализирую Alembic..."
  flask db init
fi

echo "➡️ Генерация миграций..."
flask db migrate -m "auto migration"

echo "➡️ Применение миграций..."
flask db upgrade

echo "✅ Всё готово. Запускаю crm-сервис на порту $PORT..."
flask run --host=0.0.0.0 --port=$PORT