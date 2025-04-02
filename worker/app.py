from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import os
from flasgger import Swagger

app = Flask(__name__)

# Путь к файлу openapi.yaml
template_path = os.path.join(os.path.dirname(__file__), 'openapi.yaml')

# Инициализация Swagger с указанием пути к шаблону
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
}, template_file=template_path)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # имя сервиса Kafka из docker-compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/send-event', methods=['POST'])
def send_event():
    """
    Отправить событие в Kafka
    ---
    parameters:
      - name: data
        in: body
        required: true
        schema:
          type: object
          properties:
            event:
              type: string
            data:
              type: string
    responses:
      200:
        description: Event sent to Kafka
      400:
        description: No data provided
      500:
        description: Internal Server Error
    """
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
