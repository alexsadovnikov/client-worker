from flask import Flask, Response, request
import json

app = Flask(__name__)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify([...])

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

# 📄 Список контактов
@app.route('/entity/ContactCc', methods=['GET'])
def get_contacts():
    data = [
        {"id": "1", "name": "Иван Иванов"},
        {"id": "2", "name": "Мария Смирнова"}
    ]
    return Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 🧾 Получение кейсов
@app.route('/entity/Case', methods=['GET'])
def get_cases():
    data = [
        {"id": "101", "title": "Проблема с продуктом"},
        {"id": "102", "title": "Запрос обратной связи"}
    ]
    return Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 🧬 Метаданные для Case
@app.route('/metadata/entity/Case', methods=['GET'])
def get_case_metadata():
    data = {"fields": ["id", "title", "status"]}
    return Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 🆕 Создание любой сущности
@app.route('/entity', methods=['POST'])
def create_entity():
    data = request.json
    response = {"message": "Entity created", "data": data}
    return Response(json.dumps(response, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 📤 Обновление сущности
@app.route('/entity/<entity>/<entity_id>', methods=['PUT'])
def update_entity(entity, entity_id):
    data = request.json
    response = {
        "message": f"{entity} с ID {entity_id} обновлён",
        "updated": data
    }
    return Response(json.dumps(response, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 🔎 Поиск контактов
@app.route('/entity/search/ContactCc', methods=['POST'])
def search_contacts():
    query = request.json
    data = [
        {"id": "1", "name": "Найден Иван"},
        {"id": "2", "name": "Найдена Мария"}
    ]
    return Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 🔗 Связь контакта и кейсов
@app.route('/relationship/ContactCc/<contact_id>/Case', methods=['GET'])
def get_contact_cases(contact_id):
    data = [
        {"case_id": "101", "contact_id": contact_id},
        {"case_id": "102", "contact_id": contact_id}
    ]
    return Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")

# 👤 Для примера: получить клиента
@app.route('/client/<client_id>', methods=['GET'])
def get_client(client_id):
    data = {
        "client_id": client_id,
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    }
    return Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
