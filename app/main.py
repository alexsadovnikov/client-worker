import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from flask import Flask, jsonify, request
from flasgger import Swagger
from schemas.contact import Contact
from schemas.case import Case
from schemas.agent import Agent
from schemas.call import Call
from schemas.interaction import Interaction
from pydantic import ValidationError

app = Flask(__name__)

# ✅ Конфигурация Swagger и определения моделей
app.config['SWAGGER'] = {
    'title': 'ClientService API',
    'uiversion': 3,
    'definitions': {
        'Case': Case.model_json_schema(),
        'Contact': Contact.model_json_schema(),
        'Agent': Agent.model_json_schema(),
        'Call': Call.model_json_schema(),
        'Interaction': Interaction.model_json_schema()
    }
}

swagger = Swagger(app)

# 🔹 Контакты
@app.route('/contacts', methods=['GET'])
def get_contacts():
    """Получить список контактов"""
    return jsonify([
        Contact(id=1, name="Иван Иванов", email="ivan@example.com").dict(),
        Contact(id=2, name="Мария Смирнова", email="maria@example.com").dict()
    ])

@app.route('/contacts', methods=['POST'])
def create_contact():
    """Создать контакт"""
    try:
        contact = Contact(**request.json)
        return jsonify({"message": "Contact created", "contact": contact.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/contacts/<contact_id>', methods=['GET'])
def get_contact(contact_id):
    """Получить контакт по ID"""
    return jsonify({"id": contact_id, "name": "Test", "email": "test@example.com"})

@app.route('/contacts/<contact_id>', methods=['PUT'])
def update_contact(contact_id):
    """Обновить контакт"""
    try:
        contact = Contact(**request.json)
        return jsonify({"message": f"Contact {contact_id} updated", "updated": contact.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/contacts/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """Удалить контакт"""
    return jsonify({"message": f"Contact {contact_id} deleted"})


# 🔹 Кейсы
@app.route('/cases', methods=['GET'])
def get_cases():
    """Получить список кейсов"""
    return jsonify([
        Case(id="101", title="Проблема с продуктом", status="open").dict(),
        Case(id="102", title="Запрос информации", status="closed").dict()
    ])

@app.route('/cases', methods=['POST'])
def create_case():
    """Создать кейс"""
    try:
        case = Case(**request.json)
        return jsonify({"message": "Case created", "case": case.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/cases/<case_id>', methods=['GET'])
def get_case(case_id):
    """Получить кейс по ID"""
    return jsonify({"id": case_id, "title": "Demo", "status": "open"})

@app.route('/cases/<case_id>', methods=['PUT'])
def update_case(case_id):
    """Обновить кейс"""
    try:
        case = Case(**request.json)
        return jsonify({"message": f"Case {case_id} updated", "updated": case.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/cases/<case_id>', methods=['DELETE'])
def delete_case(case_id):
    """Удалить кейс"""
    return jsonify({"message": f"Case {case_id} deleted"})


# 🔹 Звонки
@app.route('/calls', methods=['GET'])
def get_calls():
    """Получить список звонков"""
    return jsonify([])

@app.route('/calls', methods=['POST'])
def create_call():
    """Создать звонок"""
    try:
        call = Call(**request.json)
        return jsonify({"message": "Call created", "call": call.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/calls/<call_id>', methods=['GET'])
def get_call(call_id):
    """Получить звонок по ID"""
    return jsonify({"id": call_id, "agent_id": "1", "contact_id": "2"})

@app.route('/calls/<call_id>', methods=['PUT'])
def update_call(call_id):
    """Обновить звонок"""
    try:
        call = Call(**request.json)
        return jsonify({"message": f"Call {call_id} updated", "updated": call.dict()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@app.route('/calls/<call_id>', methods=['DELETE'])
def delete_call(call_id):
    """Удалить звонок"""
    return jsonify({"message": f"Call {call_id} deleted"})


@app.route('/')
def index():
    return '🚀 ClientService API is running. Перейдите на /apidocs для Swagger UI.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
