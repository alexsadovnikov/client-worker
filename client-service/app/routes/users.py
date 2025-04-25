from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from flasgger import swag_from

users_bp = Blueprint('users', __name__)

@users_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Users'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': UserCreate.schema(),
            'description': 'User data'
        }
    ],
    'responses': {
        201: {
            'description': 'User created',
            'schema': UserOut.schema()
        },
        400: {
            'description': 'Validation error'
        }
    }
})
def create_user():
    data = request.json
    user_data = UserCreate(**data)
    user = User(**user_data.dict())
    db.session.add(user)
    db.session.commit()
    return jsonify(UserOut.from_orm(user).dict()), 201


@users_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Users'],
    'responses': {
        200: {
            'description': 'List of users',
            'schema': {
                'type': 'array',
                'items': UserOut.schema()
            }
        }
    }
})
def get_users():
    users = User.query.all()
    return jsonify([UserOut.from_orm(user).dict() for user in users]), 200
