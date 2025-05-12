from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send
from pathlib import Path
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# 📦 Работа с файлами storage.json
STORAGE_PATH = Path(__file__).resolve().parent.parent / "storage.json"

def load_projects():
    if STORAGE_PATH.exists():
        with open(STORAGE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_projects(projects):
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)

# ✅ REST-эндпоинты
@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify(load_projects())

@app.route("/projects", methods=["POST"])
def create_project():
    data = request.json
    projects = load_projects()
    new_id = max([p["id"] for p in projects], default=0) + 1
    new_project = {
        "id": new_id,
        "title": data.get("title"),
        "manager": data.get("manager"),
        "client": data.get("client"),
        "status": data.get("status", "Неразобранное")
    }
    projects.append(new_project)
    save_projects(projects)
    socketio.emit("new_project", new_project)  # 🔄 Уведомление по сокету
    return jsonify(new_project), 201

# 🩺 Проверка
@app.route('/ping', methods=['GET'])
def ping():
    return {"status": "pong"}

# 🔌 WebSocket-обработчики
@socketio.on('message')
def handle_message(message):
    print(f"📨 Получено сообщение: {message}")
    send(f"Эхо: {message}", broadcast=True)

@socketio.on('connect')
def handle_connect():
    print("✅ Пользователь подключился")

@socketio.on('disconnect')
def handle_disconnect():
    print("❌ Пользователь отключился")

if __name__ == "__main__":
    print("🚀 Запуск chat WebSocket-сервера...")
    socketio.run(app, host="0.0.0.0", port=5002)