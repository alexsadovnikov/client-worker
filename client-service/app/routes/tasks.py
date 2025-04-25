from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskOut
from flasgger import swag_from

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TaskCreate.schema(),
            'description': 'Task data'
        }
    ],
    'responses': {
        201: {
            'description': 'Task created',
            'schema': TaskOut.schema()
        },
        400: {
            'description': 'Validation error'
        }
    }
})
def create_task():
    data = request.json
    task_data = TaskCreate(**data)
    task = Task(**task_data.dict())
    db.session.add(task)
    db.session.commit()
    return jsonify(TaskOut.from_orm(task).dict()), 201


@tasks_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Tasks'],
    'responses': {
        200: {
            'description': 'List of tasks',
            'schema': {
                'type': 'array',
                'items': TaskOut.schema()
            }
        }
    }
})
def get_tasks():
    tasks = Task.query.all()
    return jsonify([TaskOut.from_orm(task).dict() for task in tasks]), 200
