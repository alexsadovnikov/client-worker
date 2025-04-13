import sys
from pathlib import Path

# ✅ Добавим путь к worker/ — это важно для импорта schemas при запуске из pytest
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
from schemas.contact import Contact
from schemas.case import Case
from schemas.agent import Agent
from schemas.call import Call
from schemas.interaction import Interaction
from pydantic import ValidationError

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# ✅ Swagger с авторизацией через JWT
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


# 🔑 JWT login
@app.route('/login', methods=['POST'])
def login():
    """Логин и выдача токена"""
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
    """Пример защищённого маршрута"""
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"msg": "Missing Authorization Header"}), 401


# 🔹 Контакты
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

@app.route('/contacts/<contact_id>', methods=['GET'])
def get_contact(contact_id):
    return jsonify({"id": contact_id, "name": "Test", "email": "test@example.com"})

@app.route('/contacts/<contact_id>', methods=['PUT'])
def update_contact(contact_id):
    try:
        contact = Contact(**request.json)
        return jsonify({"message": f"Contact {contact_id} updated", "updated": contact.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/contacts/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    return jsonify({"message": f"Contact {contact_id} deleted"})


# 🔹 Кейсы
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

@app.route('/cases/<case_id>', methods=['GET'])
def get_case(case_id):
    return jsonify({"id": case_id, "title": "Demo", "status": "open"})

@app.route('/cases/<case_id>', methods=['PUT'])
def update_case(case_id):
    try:
        case = Case(**request.json)
        return jsonify({"message": f"Case {case_id} updated", "updated": case.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/cases/<case_id>', methods=['DELETE'])
def delete_case(case_id):
    return jsonify({"message": f"Case {case_id} deleted"})


# 🔹 Звонки
@app.route('/calls', methods=['GET'])
def get_calls():
    return jsonify([])

@app.route('/calls', methods=['POST'])
def create_call():
    try:
        call = Call(**request.json)
        return jsonify({"message": "Call created", "call": call.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/calls/<call_id>', methods=['GET'])
def get_call(call_id):
    return jsonify({"id": call_id, "agent_id": "1", "contact_id": "2"})

@app.route('/calls/<call_id>', methods=['PUT'])
def update_call(call_id):
    try:
        call = Call(**request.json)
        return jsonify({"message": f"Call {call_id} updated", "updated": call.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/calls/<call_id>', methods=['DELETE'])
def delete_call(call_id):
    return jsonify({"message": f"Call {call_id} deleted"})


@app.route('/')
def index():
    return '🚀 ClientService API is running. Перейдите на /apidocs для Swagger UI.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
