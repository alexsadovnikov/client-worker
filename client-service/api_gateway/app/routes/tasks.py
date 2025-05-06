from flask import Blueprint, jsonify, request
from app.schemas.task import TaskCreate, TaskUpdate
from flasgger import swag_from

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/tasks", methods=["GET"])
@swag_from("docs/tasks/get_tasks.yml")
def get_tasks():
    return jsonify([
        {"id": 1, "title": "Fix bugs", "status": "in_progress"}
    ])

@tasks_bp.route("/tasks", methods=["POST"])
@swag_from("docs/tasks/create_task.yml")
def create_task():
    data = request.get_json()
    task = TaskCreate(**data)
    return jsonify(task.dict()), 201

@tasks_bp.route("/tasks/<int:task_id>", methods=["GET"])
@swag_from("docs/tasks/get_task_by_id.yml")
def get_task(task_id):
    return jsonify({"id": task_id})

@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
@swag_from("docs/tasks/update_task.yml")
def update_task(task_id):
    data = request.get_json()
    task_update = TaskUpdate(**data)
    return jsonify({"id": task_id, **task_update.dict()})

@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@swag_from("docs/tasks/delete_task.yml")
def delete_task(task_id):
    return jsonify({"message": f"Task {task_id} deleted"})