import json
import time
import requests
from kafka import KafkaProducer, KafkaConsumer

BASE_URL = "http://crm:5000"
HEADERS = {"Auth": "mock-token", "GroupingId": "test-group"}

producer = None

def create_kafka_producer():
    global producer
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("✅ Kafka producer подключён")
            break
        except Exception as e:
            print(f"⏳ Ожидаем Kafka...: {e}")
            time.sleep(3)

def consume_from_kafka():
    while True:
        try:
            consumer = KafkaConsumer(
                'client-topic',
                bootstrap_servers='kafka:9092',
                group_id='client-consumer-group',
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                auto_offset_reset='earliest',
                enable_auto_commit=True
            )
            print("✅ Kafka consumer подключён")
            break
        except Exception as e:
            print(f"⏳ Ожидаем Kafka (consumer)...: {e}")
            time.sleep(3)

    for msg in consumer:
        event = msg.value
        print(f"📥 Получено из Kafka: {event}")
        try:
            resp = requests.post(f"{BASE_URL}/entity", json=event, headers=HEADERS)
            print(f"📬 Отправлено в CRM → {resp.status_code}: {resp.text}")
        except Exception as e:
            print(f"❌ Ошибка при отправке в CRM: {e}")