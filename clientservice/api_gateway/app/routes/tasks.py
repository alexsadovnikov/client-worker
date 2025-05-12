from flask import Blueprint
from flask_smorest import abort
from app.schemas.task import TaskCreate, TaskUpdate, TaskSchema

# Создание Blueprint с поддержкой flask_smorest
from flask_smorest import Blueprint

tasks_bp = Blueprint("tasks", "tasks", url_prefix="/tasks", description="Операции с задачами")


@tasks_bp.route("/", methods=["GET"])
@tasks_bp.response(200, TaskSchema(many=True))
def get_tasks():
    # Вернуть список задач (пока статично)
    return [{"id": 1, "title": "Fix bugs", "status": "in_progress"}]


@tasks_bp.route("/", methods=["POST"])
@tasks_bp.arguments(TaskCreate)
@tasks_bp.response(201, TaskSchema)
def create_task(task_data):
    # Создание задачи с переданными данными
    return task_data


@tasks_bp.route("/<int:task_id>", methods=["GET"])
@tasks_bp.response(200, TaskSchema)
def get_task(task_id):
    # Получение задачи по ID
    task = {"id": task_id, "title": "Example task", "status": "completed"}
    if not task:
        abort(404, message="Task not found")
    return task


@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@tasks_bp.arguments(TaskUpdate)
@tasks_bp.response(200, TaskSchema)
def update_task(task_data, task_id):
    # Обновление задачи
    updated_task = {"id": task_id, **task_data}
    return updated_task


@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@tasks_bp.response(200)
def delete_task(task_id):
    # Удаление задачи
    return {"message": f"Task {task_id} deleted"}