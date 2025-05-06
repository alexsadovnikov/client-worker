# app/routes/projects.py
from flask import Blueprint, request, jsonify
from app.db import db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from pydantic import ValidationError

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([p.to_dict() for p in projects])

@projects_bp.route("/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict())

@projects_bp.route("/", methods=["POST"])
def create_project():
    try:
        data = ProjectCreate(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    new_project = Project(**data.dict())
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.to_dict()), 201

@projects_bp.route("/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    try:
        data = ProjectUpdate(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    for field, value in data.dict(exclude_unset=True).items():
        setattr(project, field, value)
    db.session.commit()
    return jsonify(project.to_dict())

@projects_bp.route("/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return '', 204