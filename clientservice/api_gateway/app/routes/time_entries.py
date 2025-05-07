from flask import Blueprint, request, jsonify
from app.models.timesheet import TimeEntry
from app.db import db
from app.schemas.timesheet import TimeEntrySchema, TimeEntryCreate, TimeEntryUpdate
from pydantic import ValidationError

time_entries_bp = Blueprint("time_entries", __name__)
schema_out = TimeEntrySchema

@time_entries_bp.route("/", methods=["GET"])
def get_time_entries():
    entries = TimeEntry.query.all()
    return jsonify([schema_out.from_orm(e).dict() for e in entries])

@time_entries_bp.route("/", methods=["POST"])
def create_time_entry():
    try:
        entry_data = TimeEntryCreate(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    entry = TimeEntry(**entry_data.dict())
    db.session.add(entry)
    db.session.commit()
    return jsonify(schema_out.from_orm(entry).dict()), 201

@time_entries_bp.route("/<int:entry_id>", methods=["PUT"])
def update_time_entry(entry_id):
    entry = TimeEntry.query.get_or_404(entry_id)
    try:
        updated = TimeEntryUpdate(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    for key, value in updated.dict(exclude_unset=True).items():
        setattr(entry, key, value)
    db.session.commit()
    return jsonify(schema_out.from_orm(entry).dict())

@time_entries_bp.route("/<int:entry_id>", methods=["DELETE"])
def delete_time_entry(entry_id):
    entry = TimeEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return '', 204