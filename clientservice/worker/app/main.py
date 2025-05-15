from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_smorest import Api, Blueprint
from marshmallow import Schema, fields

# ✅ Относительные импорты для Docker-среды:
from shared.schemas.contact import Contact
from shared.schemas.case import Case
from shared.schemas.agent import Agent
from shared.schemas.call import Call
from shared.schemas.interaction import Interaction
from shared.schemas.message import MessageCreate as Message

from pydantic import ValidationError

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    app.config['API_TITLE'] = 'ClientService API'
    app.config['API_VERSION'] = '1.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/apidocs'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    app.config['PROPAGATE_EXCEPTIONS'] = True  # ✅ важно для JWT ошибок

    api = Api(app)
    jwt = JWTManager(app)

    # ---------- Marshmallow схемы ----------
    class ContactSchema(Schema):
        id = fields.Int()
        name = fields.Str()
        email = fields.Email()

    class CaseSchema(Schema):
        id = fields.Str()
        title = fields.Str()
        status = fields.Str()

    class CallResponseSchema(Schema):
        message = fields.Str()
        call = fields.Dict()

    class MessageResponseSchema(Schema):
        message = fields.Str()
        data = fields.Dict()

    # ---------- Роуты ----------
    auth_blp = Blueprint("auth", "auth", description="JWT Аутентификация")

    @auth_blp.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        if data.get("username") == "admin" and data.get("password") == "admin":
            return jsonify(access_token=create_access_token(identity="admin"))
        return jsonify({"msg": "Bad credentials"}), 401

    @auth_blp.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        return jsonify(logged_in_as=get_jwt_identity())

    api.register_blueprint(auth_blp, url_prefix="/auth")

    main_blp = Blueprint("main", "main", description="Основные маршруты")

    @main_blp.route('/contacts', methods=['GET'])
    @main_blp.response(200, ContactSchema(many=True))
    def get_contacts():
        return [
            Contact(id=1, name="Иван", email="ivan@example.com").dict(),
            Contact(id=2, name="Мария", email="maria@example.com").dict()
        ]

    @main_blp.route('/cases', methods=['GET'])
    @main_blp.response(200, CaseSchema(many=True))
    def get_cases():
        return [
            Case(id="1", title="Проблема", status="open").dict()
        ]

    @main_blp.route('/calls', methods=['POST'])
    @main_blp.response(200, CallResponseSchema)
    def create_call():
        try:
            call = Call(**request.json)
            return {"message": "Call created", "call": call.dict()}
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

    @main_blp.route('/messages/send', methods=['POST'])
    @jwt_required()
    @main_blp.response(200, MessageResponseSchema)
    def send_message():
        try:
            msg = Message(**request.json)
            return {"message": "Сообщение принято", "data": msg.dict()}
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

    @main_blp.route('/send', methods=['POST'])
    def send_event():
        data = request.get_json()
        return jsonify({"code": 200, "status": "Event received", "data": data})

    @main_blp.route('/crm/contacts', methods=['GET'])
    def get_mock_contacts():
        return jsonify([
            {"id": 1, "name": "Иван", "email": "ivan@example.com"},
            {"id": 2, "name": "Мария", "email": "maria@example.com"}
        ])

    @main_blp.route('/', methods=['GET'])
    def index():
        return '🚀 ClientService API is running. Перейдите на /apidocs для Swagger UI.'

    api.register_blueprint(main_blp, url_prefix="/")

    return app