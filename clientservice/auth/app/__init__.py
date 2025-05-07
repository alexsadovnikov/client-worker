from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_smorest import Api

from clientservice.auth.app.routes.auth import auth_blp

def create_app():
    app = Flask(__name__)

    # ✅ Конфигурация OpenAPI / Swagger
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    app.config["API_TITLE"] = "Auth Service API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/apidocs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # ✅ Инициализация расширений
    CORS(app)
    JWTManager(app)

    # ✅ Flask-Smorest API
    api = Api(app)
    api.register_blueprint(auth_blp)

    # 🟢 Проверка статуса сервиса
    @app.route("/")
    def index():
        return jsonify({"status": "Auth Service is running"}), 200

    return app