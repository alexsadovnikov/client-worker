#!/bin/bash

echo "➡️ Запускаем auth-сервис..."

cd "$(dirname "$0")" || exit 1
export FLASK_APP=app:create_app
export FLASK_ENV=development

flask run --port=5059