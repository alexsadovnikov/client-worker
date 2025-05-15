from flask import Flask
from flask_smorest import Api, Blueprint

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "My Service API"
    app.config["API_VERSION"] = "1.0.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/apidocs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    blp = Blueprint("my_service", __name__, description="Test endpoints")

    @blp.route("/ping")
    def ping():
        return {"message": "pong"}

    api.register_blueprint(blp)
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5004)