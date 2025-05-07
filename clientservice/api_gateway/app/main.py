from flask import Flask, send_from_directory, jsonify
from flask_migrate import Migrate
from app.db import db
import yaml
import os

# 🔹 Импорт моделей (для Alembic и SQLAlchemy)
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.models.expense import Expense
from app.models.timesheet import TimeEntry
from app.models.analytics import Analytics
from app.models.financial import Financial

# 🔹 Инициализация Flask-приложения
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)

# 🔹 Конфигурация PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://client_user:client_pass@db:5432/client_service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔹 Инициализация SQLAlchemy и Alembic
db.init_app(app)
migrate = Migrate(app, db)

# 🔹 Импорт и регистрация всех маршрутов
from app.routes.projects import projects_bp
from app.routes.tasks import tasks_bp
from app.routes.users import users_bp
from app.routes.expenses import expenses_bp
from app.routes.timesheets import timesheets_bp
from app.routes.time_entries import time_entries_bp
from app.routes.analytics import analytics_bp
from app.routes.financials import financials_bp

# 🔹 Регистрация Blueprints
app.register_blueprint(projects_bp, url_prefix="/projects")
app.register_blueprint(tasks_bp, url_prefix="/tasks")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(expenses_bp, url_prefix="/expenses")
app.register_blueprint(timesheets_bp, url_prefix="/timesheets")
app.register_blueprint(time_entries_bp, url_prefix="/time-entries")
app.register_blueprint(analytics_bp, url_prefix="/analytics")
app.register_blueprint(financials_bp, url_prefix="/financials")

# 🔹 Swagger UI и документация
@app.route('/apidocs/')
def swagger_ui():
    return send_from_directory(app.static_folder, 'swagger-ui.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/openapi.yaml')
def openapi_yaml():
    with open(os.path.join(app.static_folder, 'openapi.yaml'), 'r') as f:
        return f.read(), 200, {'Content-Type': 'text/yaml'}

@app.route('/openapi.json')
def openapi_json():
    with open(os.path.join(app.static_folder, 'openapi.yaml'), 'r') as f:
        yaml_content = yaml.safe_load(f)
    return jsonify(yaml_content)

# 🔹 Системные тестовые эндпоинты
@app.route('/')
def index():
    return {"message": "API Gateway is running"}

@app.route('/ping', methods=['GET'])
def ping():
    return {"status": "ok"}

# 🔹 Точка входа
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)