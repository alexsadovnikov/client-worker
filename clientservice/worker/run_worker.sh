#!/bin/bash

echo "➡️ Переход в папку worker..."
cd "$(dirname "$0")" || exit 1

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Устанавливаю переменные среды..."
export PYTHONPATH=.
export FLASK_APP=app.main:create_app
export FLASK_RUN_PORT=5050

echo "➡️ Проверяю порт 5050..."
PORT=5050
PID=$(lsof -ti tcp:$PORT)
if [ ! -z "$PID" ]; then
  echo "⚠️ Найден процесс на порту $PORT (PID=$PID), убиваю его..."
  kill -9 $PID
fi

echo "➡️ Генерация OpenAPI (если необходимо)..."
python3 -c "import yaml, json; f=open('static/openapi.yaml'); j=json.dumps(yaml.safe_load(f), indent=2, ensure_ascii=False); open('static/openapi.json','w').write(j)"

echo "✅ Запуск worker-сервиса..."
flask run --host=0.0.0.0 --port=$PORT