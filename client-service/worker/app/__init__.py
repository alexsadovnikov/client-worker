from flask import Flask
from flasgger import Swagger


def create_app():
    app = Flask(__name__)

    # Подключаем Swagger с кастомным openapi.yaml (если есть)
    swagger = Swagger(app, template_file='static/openapi.yaml')

    # Регистрируем все маршруты
    try:
        from .routes import register_routes
        register_routes(app)
    except ImportError:
        print("⚠️ Предупреждение: не удалось импортировать register_routes")

    return app
