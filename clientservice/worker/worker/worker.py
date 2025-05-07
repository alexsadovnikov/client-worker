import os
import json
import time
import threading
import requests
from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

app = Flask(__name__)

SWAGGER_URL = '/apidocs'
API_URL = '/static/openapi.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Client Worker API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

BASE_URL = "http://crm:5000"
HEADERS = {"Auth": "mock-token", "GroupingId": "test-group"}

producer = None

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

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Service is running"}), 200

@app.route("/send", methods=["POST"])
def send_event():
    data = request.get_json()
    if not data or 'client_id' not in data or 'message' not in data:
        return jsonify({"error": "Некорректный формат запроса"}), 400

    event = {"client_id": data['client_id'], "message": data['message']}
    try:
        producer.send('client-topic', value=event)
        print(f"📤 Отправлено в Kafka: {event}")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"❌ Ошибка при отправке в Kafka: {e}")
        return jsonify({"error": str(e)}), 500

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

if __name__ == "__main__":
    create_kafka_producer()
    consumer_thread = threading.Thread(target=consume_from_kafka)
    consumer_thread.daemon = True
    consumer_thread.start()
    app.run(host="0.0.0.0", port=5050)
