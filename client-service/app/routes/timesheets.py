from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.timesheet import TimeEntry
from app.schemas.timesheet import TimesheetCreate, TimesheetOut
from flasgger import swag_from

timesheets_bp = Blueprint('timesheets', __name__)

@timesheets_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Timesheets'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': TimesheetCreate.schema(),
            'required': True
        }
    ],
    'responses': {
        201: {
            'description': 'Created',
            'schema': TimesheetOut.schema()
        }
    }
})
def create_timesheet():
    data = request.json
    entry_data = TimesheetCreate(**data)
    entry = TimeEntry(**entry_data.dict())
    db.session.add(entry)
    db.session.commit()
    return jsonify(TimesheetOut.from_orm(entry).dict()), 201

@timesheets_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Timesheets'],
    'responses': {
        200: {
            'description': 'List of time entries',
            'schema': {
                'type': 'array',
                'items': TimesheetOut.schema()
            }
        }
    }
})
def get_timesheets():
    entries = TimeEntry.query.all()
    return jsonify([TimesheetOut.from_orm(e).dict() for e in entries]), 200
