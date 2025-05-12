#!/bin/bash

# Генерация openapi.json во всех микросервисах с использованием Flask-Smorest
echo "🔄 Генерация openapi.json для всех микросервисов..."

# Папка с сервисами
SERVICES_DIR="./clientservice"

# Найдём все main.py в микросервисах
find "$SERVICES_DIR" -name "main.py" | while read main_path; do
    SERVICE_DIR=$(dirname "$main_path")
    SERVICE_NAME=$(basename "$(dirname "$SERVICE_DIR")")

    echo "📦 [$SERVICE_NAME] Генерация openapi.json..."
    FLASK_APP="$main_path" flask openapi > "$SERVICE_DIR/static/openapi.json"
    echo "✅ [$SERVICE_NAME] Сохранено в $SERVICE_DIR/static/openapi.json"
done

echo "🎉 Генерация завершена."