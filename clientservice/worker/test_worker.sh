#!/bin/bash

# === Аргументы с фолбэком ===
SENDER_ID=${1:-"1"}
RECIPIENT_ID=${2:-"2"}
CONTENT=${3:-"Привет из test_worker.sh"}

# === 1. Авторизация ===
echo "🔐 Авторизация..."
TOKEN=$(curl -s -X POST http://localhost:5050/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}' | jq -r '.access_token')

if [ "$TOKEN" = "null" ] || [ -z "$TOKEN" ]; then
  echo "❌ Не удалось получить токен"
  exit 1
fi

echo "✅ Токен получен"
echo "ACCESS_TOKEN=$TOKEN" > .env

# === 2. Проверка защищённого маршрута ===
echo "🔎 Проверка доступа..."
curl -s -X GET http://localhost:5050/auth/protected \
  -H "Authorization: Bearer $TOKEN"
echo ""

# === 3. Отправка сообщения ===
echo "📤 Отправка сообщения в /messages/send..."
curl -s -X POST http://localhost:5050/messages/send \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"sender_id\": \"$SENDER_ID\",
    \"recipient_id\": \"$RECIPIENT_ID\",
    \"content\": \"$CONTENT\"
  }"
echo ""