from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_smorest import Api
from flask_cors import CORS

from clientservice.auth.app.routes.auth import auth_blp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["API_TITLE"] = "Auth Service API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/apidocs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

CORS(app)
JWTManager(app)

api = Api(app)
api.register_blueprint(auth_blp)

@app.route("/")
def index():
    return jsonify({"status": "Auth Service is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)