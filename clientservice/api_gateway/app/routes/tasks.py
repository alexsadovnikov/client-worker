from flask import request
from flask_smorest import Blueprint
from app.schemas.task import TaskCreate, TaskUpdate
from app.schemas.task_marshmallow import TaskSchema

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks", description="Управление задачами")

tasks = [
    {"id": 1, "title": "Fix bugs", "status": "in_progress"},
    {"id": 2, "title": "Write tests", "status": "pending"}
]

@tasks_bp.route("/")
@tasks_bp.response(200, TaskSchema(many=True))
def get_tasks():
    return tasks

@tasks_bp.route("/", methods=["POST"])
@tasks_bp.arguments(TaskCreate)
@tasks_bp.response(201, TaskSchema)
def create_task(new_data):
    new_task = {"id": len(tasks) + 1, **new_data}
    tasks.append(new_task)
    return new_task

@tasks_bp.route("/<int:task_id>")
@tasks_bp.response(200, TaskSchema)
def get_task(task_id):
    return next((task for task in tasks if task["id"] == task_id), {"id": task_id, "title": "Not found"})

@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@tasks_bp.arguments(TaskUpdate)
@tasks_bp.response(200, TaskSchema)
def update_task(update_data, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task.update(update_data)
            return task
    return {"id": task_id, "title": "Not found"}

@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": f"Task {task_id} deleted"}