from flask import Flask, jsonify, request

app = Flask(__name__)

# 📄 Список контактов
@app.route('/entity/ContactCc', methods=['GET'])
def get_contacts():
    return jsonify([
        {"id": "1", "name": "Иван Иванов"},
        {"id": "2", "name": "Мария Смирнова"}
    ])

# 🧾 Получение кейсов
@app.route('/entity/Case', methods=['GET'])
def get_cases():
    return jsonify([
        {"id": "101", "title": "Проблема с продуктом"},
        {"id": "102", "title": "Запрос обратной связи"}
    ])

# 🧬 Метаданные для Case
@app.route('/metadata/entity/Case', methods=['GET'])
def get_case_metadata():
    return jsonify({
        "fields": ["id", "title", "status"]
    })

# 🆕 Создание любой сущности
@app.route('/entity', methods=['POST'])
def create_entity():
    data = request.json
    return jsonify({"message": "Entity created", "data": data})

# 📤 Обновление сущности
@app.route('/entity/<entity>/<entity_id>', methods=['PUT'])
def update_entity(entity, entity_id):
    data = request.json
    return jsonify({
        "message": f"{entity} with ID {entity_id} updated",
        "updated": data
    })

# 🔎 Поиск контактов
@app.route('/entity/search/ContactCc', methods=['POST'])
def search_contacts():
    query = request.json
    return jsonify([
        {"id": "1", "name": "Найден Иван"},
        {"id": "2", "name": "Найдена Мария"}
    ])

# 🔗 Связь контакта и кейсов
@app.route('/relationship/ContactCc/<contact_id>/Case', methods=['GET'])
def get_contact_cases(contact_id):
    return jsonify([
        {"case_id": "101", "contact_id": contact_id},
        {"case_id": "102", "contact_id": contact_id}
    ])

# 👤 Для примера: получить клиента
@app.route('/client/<client_id>', methods=['GET'])
def get_client(client_id):
    return jsonify({
        "client_id": client_id,
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
