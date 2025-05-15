from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from shared.schemas.user import UserLogin
from pydantic import ValidationError
from flask_smorest import Blueprint as SmorestBlueprint

auth_bp = SmorestBlueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
@auth_bp.response(200, description="Успешная аутентификация")
def login():
    data = request.get_json()
    user = UserLogin(**data)
    access_token = create_access_token(identity=user.email)
    return {"access_token": access_token}