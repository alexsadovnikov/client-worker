# worker/consumer.py
from kafka import KafkaConsumer
import json
import requests

consumer = KafkaConsumer(
    'client-topic',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    group_id='client-worker-group'
)

print("🟢 Kafka Consumer запущен и ожидает сообщений...")

for message in consumer:
    data = message.value
    print("📥 Получено сообщение:", data)

    # Пример запроса в mock CRM (можно заменить URL и формат)
    try:
        response = requests.post("http://crm:5000/api/messages", json=data)
        print("📤 Отправлено в CRM:", response.status_code)
    except Exception as e:
        print("❌ Ошибка отправки в CRM:", str(e))
