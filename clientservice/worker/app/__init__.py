from flask import Flask


def create_app():
    app = Flask(__name__)

    # Регистрируем все маршруты, если есть функция register_routes
    try:
        from .routes import register_routes
        register_routes(app)
    except ImportError:
        print("⚠️ Предупреждение: не удалось импортировать register_routes")

    return app