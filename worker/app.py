from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # имя сервиса Kafka из docker-compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/send-event', methods=['POST'])
def send_event():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        producer.send('client-events', value=data)
        producer.flush()
        return jsonify({'status': 'Event sent to Kafka'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
