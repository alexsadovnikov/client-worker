from flask import Blueprint, jsonify, request
from app.schemas.user import UserCreate, UserUpdate, UserOut
from flask_smorest import Blueprint

users_bp = Blueprint("users", __name__, url_prefix="/users", description="Управление пользователями")

fake_users = [
    {"id": 1, "email": "user@example.com", "name": "Иван Иванов", "role": "admin"}
]

@users_bp.route("/")
@users_bp.response(200, UserOut(many=True))
def get_users():
    return fake_users

@users_bp.route("/", methods=["POST"])
@users_bp.arguments(UserCreate)
@users_bp.response(201, UserOut)
def create_user(data):
    new_user = {"id": len(fake_users) + 1, **data}
    fake_users.append(new_user)
    return new_user

@users_bp.route("/<int:user_id>")
@users_bp.response(200, UserOut)
def get_user(user_id):
    return next((u for u in fake_users if u["id"] == user_id), {"id": user_id, "email": "N/A", "name": "Not found", "role": "unknown"})

@users_bp.route("/<int:user_id>", methods=["PUT"])
@users_bp.arguments(UserUpdate)
@users_bp.response(200, UserOut)
def update_user(data, user_id):
    for user in fake_users:
        if user["id"] == user_id:
            user.update(data)
            return user
    return {"id": user_id, "email": "N/A", "name": "Not found", "role": "unknown"}

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global fake_users
    fake_users = [u for u in fake_users if u["id"] != user_id]
    return {"message": f"User {user_id} deleted"}