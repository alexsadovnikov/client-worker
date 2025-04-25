# app/routes/projects.py
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectOut
from flasgger import swag_from

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/", methods=["POST"])
@swag_from({
    "tags": ["Projects"],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": ProjectCreate.schema()
            }
        }
    },
    "responses": {
        201: {
            "description": "Project created",
            "content": {
                "application/json": {
                    "schema": ProjectOut.schema()
                }
            }
        }
    }
})
def create_project():
    data = request.get_json()
    project_data = ProjectCreate(**data)
    project = Project(**project_data.dict())
    db.session.add(project)
    db.session.commit()
    return jsonify(ProjectOut.from_orm(project).dict()), 201

@projects_bp.route("/", methods=["GET"])
@swag_from({
    "tags": ["Projects"],
    "responses": {
        200: {
            "description": "List of projects",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": ProjectOut.schema()
                    }
                }
            }
        }
    }
})
def get_projects():
    projects = Project.query.all()
    return jsonify([ProjectOut.from_orm(p).dict() for p in projects]), 200
