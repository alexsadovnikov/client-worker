#!/bin/bash

echo "➡️ Переход в папку api_gateway..."
cd ~/Documents/VM/ClientServiceDocs/client-service/api_gateway/

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Устанавливаю переменную среды FLASK_APP..."
export FLASK_APP=app.main:app

echo "➡️ Генерирую свежий openapi.json из openapi.yaml..."
python3 -c "import yaml, json; f=open('app/static/openapi.yaml'); j=json.dumps(yaml.safe_load(f), indent=2, ensure_ascii=False); open('app/static/openapi.json','w').write(j)"

echo "➡️ Запускаю автообновление openapi.json при изменении openapi.yaml..."
watchmedo shell-command \
  --patterns="*.yaml" \
  --recursive \
  --command='python3 -c "import yaml, json; f=open(\"app/static/openapi.yaml\"); j=json.dumps(yaml.safe_load(f), indent=2, ensure_ascii=False); open(\"app/static/openapi.json\",\"w\").write(j)"' \
  app/static/ &

echo "➡️ Проверяю порт 8081..."
PORT=8081
PID=$(lsof -ti tcp:$PORT)
if [ ! -z "$PID" ]; then
  echo "⚠️ Найден процесс на порту $PORT (PID=$PID), убиваю его..."
  kill -9 $PID
fi

echo "➡️ Проверяю наличие static/swagger-ui.html..."
if [ ! -f app/static/swagger-ui.html ]; then
  echo "❌ Файл swagger-ui.html не найден! Остановлено."
  exit 1
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

echo "✅ Все готово. Запускаю Flask-приложение..."
flask run --reload --host=0.0.0.0 --port=$PORT