from flask import Blueprint, jsonify, request
from app.schemas.user import UserCreate, UserUpdate, UserOut
from flasgger import swag_from

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["GET"])
@swag_from("docs/users/get_users.yml")
def get_users():
    return jsonify([])

@users_bp.route("/users", methods=["POST"])
@swag_from("docs/users/create_user.yml")
def create_user():
    data = request.get_json()
    user = UserCreate(**data)
    return jsonify(user.dict()), 201

@users_bp.route("/users/<int:user_id>", methods=["GET"])
@swag_from("docs/users/get_user_by_id.yml")
def get_user(user_id):
    return jsonify({"id": user_id})

@users_bp.route("/users/<int:user_id>", methods=["PUT"])
@swag_from("docs/users/update_user.yml")
def update_user(user_id):
    data = request.get_json()
    user_update = UserUpdate(**data)
    return jsonify({"id": user_id, **user_update.dict()})

@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
@swag_from("docs/users/delete_user.yml")
def delete_user(user_id):
    return jsonify({"message": f"User {user_id} deleted"})

@users_bp.route("/", methods=["GET"])
@swag_from({
    'responses': {
        200: {
            'description': 'Список пользователей (демо)',
            'examples': {
                'application/json': [
                    {"id": 1, "email": "user@example.com"}
                ]
            }
        }
    }
})
def get_demo_users():
    return jsonify([{"id": 1, "email": "user@example.com"}])