from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_smorest import Api, Blueprint
from marshmallow import Schema, fields

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    app.config['API_TITLE'] = 'Auth Service'
    app.config['API_VERSION'] = '1.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/apidocs'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    jwt = JWTManager(app)
    api = Api(app)

    class TokenResponse(Schema):
        access_token = fields.Str()

    class ErrorResponse(Schema):
        msg = fields.Str()

    auth_blp = Blueprint("auth", "auth", description="Аутентификация")

    @auth_blp.route('/login', methods=['POST'])
    @auth_blp.response(200, schema=TokenResponse)        # ✅ исправлено
    @auth_blp.alt_response(401, schema=ErrorResponse)     # ✅ исправлено
    def login():
        data = request.get_json()
        if data.get("username") == "admin" and data.get("password") == "admin":
            token = create_access_token(identity="admin")
            return {"access_token": token}
        return {"msg": "Неверные учетные данные"}, 401

    @auth_blp.route('/me', methods=['GET'])
    @jwt_required()
    def me():
        return {"user": get_jwt_identity()}

    @auth_blp.route('/', methods=['GET'])
    def index():
        return '🔐 Auth-сервис работает. Swagger доступен на /apidocs'

    api.register_blueprint(auth_blp, url_prefix="/auth")

    return app