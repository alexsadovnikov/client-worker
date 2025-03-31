from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import time

app = Flask(__name__)

# Подключение к Kafka с ожиданием
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

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    producer.send('client-topic', data)
    print(f"📤 Отправлено в Kafka: {data}")
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
