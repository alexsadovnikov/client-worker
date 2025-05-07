from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from clientservice.auth.app.schemas.token import LoginSchema, TokenSchema, UserInfoSchema

auth_blp = Blueprint("Auth", "auth", url_prefix="/auth", description="JWT авторизация")

@auth_blp.route("/login")
class Login(MethodView):
    @auth_blp.arguments(LoginSchema)
    @auth_blp.response(200, TokenSchema)
    def post(self, data):
        if data["username"] != "admin" or data["password"] != "admin":
            abort(401, message="Неверные учётные данные")
        token = create_access_token(identity=data["username"])
        return {"access_token": token}

@auth_blp.route("/protected")
class Protected(MethodView):
    @jwt_required()
    @auth_blp.response(200, UserInfoSchema)
    def get(self):
        current_user = get_jwt_identity()
        return {"user": current_user}

@auth_blp.route("/verify")
class VerifyToken(MethodView):
    @jwt_required()
    @auth_blp.response(200, UserInfoSchema)
    def get(self):
        current_user = get_jwt_identity()
        return {"user": current_user}