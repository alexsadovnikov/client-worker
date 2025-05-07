#!/bin/bash

echo "➡️ Переход в папку api_gateway..."
cd ~/Documents/VM/ClientServiceDocs/client-service/api_gateway/ || exit 1

echo "➡️ Активирую виртуальное окружение..."
source ../../.venv/bin/activate

echo "➡️ Генерирую свежий openapi.json из openapi.yaml..."
cd app/static/
python3 -c "import yaml, json; f=open('openapi.yaml'); j=json.dumps(yaml.safe_load(f), indent=2, ensure_ascii=False); open('openapi.json','w').write(j)"
cd ../../

echo "➡️ Проверяю порт 8081..."
PID=$(lsof -t -i:8081)

if [ -n "$PID" ]; then
    echo "⚠️ Найден процесс на порту 8081 (PID=$PID), убиваю его..."
    kill -9 "$PID"
    sleep 1
else
    echo "✅ Порт 8081 свободен."
fi

echo "➡️ Проверяю наличие static/swagger-ui.html..."
if [ ! -f app/static/swagger-ui.html ]; then
    echo "❌ Файл swagger-ui.html не найден!"
    exit 1
fi

echo "➡️ Запускаю Flask приложение на 0.0.0.0:8081..."
export FLASK_APP=app.main
flask run --host=0.0.0.0 --port=8081
