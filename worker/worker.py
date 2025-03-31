from flask import Flask, request, jsonify
from kafka import KafkaProducer
import requests
import json
import time

app = Flask(__name__)

# ===============================
# 🔌 Подключение к Kafka с ожиданием
# ===============================
producer = None
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

# ===============================
# 📤 Отправка сообщений в Kafka
# ===============================
@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    producer.send('client-topic', data)
    print(f"📨 Отправлено в Kafka: {data}")
    return jsonify({'status': 'ok'}), 200

# ===============================
# 🔗 Интеграция с mock CRM (Contact Center)
# ===============================
BASE_URL = "http://crm:5000"
HEADERS = {
    "Auth": "mock-token",
    "GroupingId": "test-group"
}

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

# ===============================
# 🚀 Запуск Flask-сервиса
# ===============================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
