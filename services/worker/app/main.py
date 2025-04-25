import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
from app.schemas.contact import Contact
from app.schemas.case import Case
from app.schemas.agent import Agent
from app.schemas.call import Call
from app.schemas.interaction import Interaction
from app.schemas.message import MessageCreate as Message
from pydantic import ValidationError

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

swagger_template = {
    "openapi": "3.0.2",
    "info": {
        "title": "ClientService API",
        "description": "API с JWT авторизацией",
        "version": "1.0"
    },
    "components": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                "description": "Введите токен в формате: Bearer <токен>"
            }
        }
    },
    "security": [{"BearerAuth": []}]
}
swagger = Swagger(app, template=swagger_template)
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad credentials"}), 401

@app.route('/protected', methods=['GET'])
@swag_from({
    'security': [{'BearerAuth': []}],
    'responses': {
        200: {'description': 'Доступ разрешён'},
        401: {'description': 'Неавторизован'}
    }
})
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"msg": "Missing Authorization Header"}), 401

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify([
        Contact(id=1, name="Иван Иванов", email="ivan@example.com").dict(),
        Contact(id=2, name="Мария Смирнова", email="maria@example.com").dict()
    ])

@app.route('/contacts', methods=['POST'])
def create_contact():
    try:
        contact = Contact(**request.json)
        return jsonify({"message": "Contact created", "contact": contact.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/cases', methods=['GET'])
def get_cases():
    return jsonify([
        Case(id="101", title="Проблема с продуктом", status="open").dict(),
        Case(id="102", title="Запрос информации", status="closed").dict()
    ])

@app.route('/cases', methods=['POST'])
def create_case():
    try:
        case = Case(**request.json)
        return jsonify({"message": "Case created", "case": case.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/calls', methods=['POST'])
def create_call():
    try:
        call = Call(**request.json)
        return jsonify({"message": "Call created", "call": call.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/messages/send', methods=['POST'])
@jwt_required()
def send_message():
    try:
        msg = Message(**request.json)
        print(f"📨 Получено сообщение: {msg.dict()}")
        return jsonify({"message": "Сообщение принято", "data": msg.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/')
def index():
    return '🚀 ClientService API is running. Перейдите на /apidocs для Swagger UI.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
