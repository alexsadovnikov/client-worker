### 🔹 clientservice/worker/app/main.py

from flask import Flask, request, jsonify
from flask_smorest import Api, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from marshmallow import Schema, fields

# 🔹 Marshmallow-схемы
class SendEventResponse(Schema):
    status = fields.String(metadata={"example": "ok"})

class ErrorResponse(Schema):
    error = fields.String(metadata={"example": "Некорректный формат запроса"})

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config['API_TITLE'] = 'Client Worker API'
    app.config['API_VERSION'] = '1.0.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'  # mounts at root
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/apidocs'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    api = Api(app)
    jwt = JWTManager(app)

    # 🔹 Роуты
    main_blp = Blueprint("worker", __name__, description="Kafka Worker API")

    @main_blp.route("/", methods=["GET"])
    def index():
        return jsonify({"message": "Service is running"}), 200

    @main_blp.route("/send", methods=["POST"])
    @main_blp.response(200, schema=SendEventResponse)
    @main_blp.alt_response(400, schema=ErrorResponse, description="Некорректный запрос")
    @main_blp.alt_response(500, schema=ErrorResponse, description="Внутренняя ошибка")
    @jwt_required()
    def send_event():
        from app.kafka import producer  # avoid circular import
        data = request.get_json()
        if not data or 'client_id' not in data or 'message' not in data:
            return {"error": "Некорректный формат запроса"}, 400

        if producer is None:
            return {"error": "Kafka producer не инициализирован"}, 500

        event = {"client_id": data['client_id'], "message": data['message']}
        try:
            producer.send('client-topic', value=event)
            print(f"📤 Отправлено в Kafka: {event}")
            return {"status": "ok"}
        except Exception as e:
            print(f"❌ Ошибка при отправке в Kafka: {e}")
            return {"error": str(e)}, 500

    api.register_blueprint(main_blp)
    return app