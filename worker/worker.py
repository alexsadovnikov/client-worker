from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
import requests
import json
import time
import threading
from flasgger import Swagger
import os

app = Flask(__name__)

# --- Swagger config ---
BASE_URL = "http://crm:5000"
HEADERS = {
    "Auth": "mock-token",
    "GroupingId": "test-group"
}

template_file_path = os.path.join(os.path.dirname(__file__), "openapi.yaml")

swagger = Swagger(app, config={
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}, template_file=template_file_path)

# --- Kafka producer (будет подключаться при запуске)
producer = None

# --- Kafka consumer loop
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

# --- Роуты

@app.route("/")
def index():
    return jsonify({"message": "Worker API is running"}), 200

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    producer.send('client-topic', data)
    producer.flush()
    return jsonify({'status': 'ok'}), 200

@app.route("/crm/contacts", methods=["GET"])
def get_contacts():
    resp = requests.get(f"{BASE_URL}/entity/ContactCc", headers=HEADERS)
    return jsonify(resp.json()), resp.status_code

@app.route("/crm/contact", methods=["POST"])
def create_contact():
    data = request.json
    resp = requests.post(f"{BASE_URL}/entity", json=data, headers=HEADERS)
    return jsonify(resp.json()), resp.status_code

@app.route("/crm/metadata/case", methods=["GET"])
def get_case_metadata():
    resp = requests.get(f"{BASE_URL}/metadata/entity/Case", headers=HEADERS)
    return jsonify(resp.json()), resp.status_code

# --- Только при запуске файла вручную:
if __name__ == '__main__':
    # подключение к Kafka producer
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("✅ Kafka producer подключён")
            break
        except Exception as e:
            print("⏳ Ожидаем Kafka...")
            time.sleep(3)

    # запуск consumer в фоне
    threading.Thread(target=consume_from_kafka, daemon=True).start()

    # запуск Flask
    app.run(host='0.0.0.0', port=5050)
