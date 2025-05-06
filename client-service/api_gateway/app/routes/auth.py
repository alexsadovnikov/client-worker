from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from shared.schemas.user import UserLogin
from pydantic import ValidationError
from flasgger import swag_from

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
@swag_from({
    "summary": "Аутентификация",
    "description": "Получение JWT токена",
    "responses": {
        200: {
            "description": "Токен авторизации",
            "examples": {
                "application/json": {
                    "access_token": "jwt-token"
                }
            }
        },
        400: {
            "description": "Ошибка валидации"
        }
    }
})
def login():
    try:
        data = request.get_json()
        user = UserLogin(**data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    # Простейшая мок-аутентификация (замени на свою логику)
    if user.email == "admin@example.com" and user.password == "securepassword":
        token = create_access_token(identity=user.email)
        return jsonify(access_token=token)
    return jsonify({"error": "Invalid credentials"}), 401