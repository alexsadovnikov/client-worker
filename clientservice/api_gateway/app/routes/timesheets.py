from flask import Blueprint, jsonify, request
from app.schemas.timesheet import TimesheetCreate, TimesheetUpdate

timesheets_bp = Blueprint("timesheets", __name__)

@timesheets_bp.route("/timesheets", methods=["GET"])
def get_timesheets():
    return jsonify([])

@timesheets_bp.route("/timesheets", methods=["POST"])
def create_timesheet():
    data = request.get_json()
    timesheet = TimesheetCreate(**data)
    return jsonify(timesheet.dict()), 201

@timesheets_bp.route("/timesheets/<int:timesheet_id>", methods=["GET"])
def get_timesheet(timesheet_id):
    return jsonify({"id": timesheet_id})

@timesheets_bp.route("/timesheets/<int:timesheet_id>", methods=["PUT"])
def update_timesheet(timesheet_id):
    data = request.get_json()
    timesheet_update = TimesheetUpdate(**data)
    return jsonify({"id": timesheet_id, **timesheet_update.dict()})

@timesheets_bp.route("/timesheets/<int:timesheet_id>", methods=["DELETE"])
def delete_timesheet(timesheet_id):
    return jsonify({"message": f"Timesheet {timesheet_id} deleted"})