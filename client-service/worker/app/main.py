
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
from shared.schemas.contact import Contact
from shared.schemas.case import Case
from shared.schemas.agent import Agent
from shared.schemas.call import Call
from shared.schemas.interaction import Interaction
from shared.schemas.message import MessageCreate as Message
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
    if data.get("username") == "admin" and data.get("password") == "admin":
        return jsonify(access_token=create_access_token(identity="admin"))
    return jsonify({"msg": "Bad credentials"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=get_jwt_identity()), 200

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify([
        Contact(id=1, name="Иван", email="ivan@example.com").dict(),
        Contact(id=2, name="Мария", email="maria@example.com").dict()
    ])

@app.route('/cases', methods=['GET'])
def get_cases():
    return jsonify([
        Case(id="1", title="Проблема", status="open").dict()
    ])

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
        return jsonify({"message": "Сообщение принято", "data": msg.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/')
def index():
    return '🚀 ClientService API is running. Перейдите на /apidocs для Swagger UI.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)