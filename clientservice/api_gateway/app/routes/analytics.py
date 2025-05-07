from flask import Blueprint, jsonify, request
from app.schemas.analytics import AnalyticsReportCreate

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/analytics/reports", methods=["GET"])
def get_reports():
    return jsonify([])

@analytics_bp.route("/analytics/reports", methods=["POST"])
def create_report():
    data = request.get_json()
    report = AnalyticsReportCreate(**data)
    return jsonify(report.dict()), 201

@analytics_bp.route("/analytics/reports/<int:report_id>", methods=["GET"])
def get_report(report_id):
    return jsonify({"id": report_id})

@analytics_bp.route("/analytics/reports/<int:report_id>", methods=["DELETE"])
def delete_report(report_id):
    return jsonify({"message": f"Report {report_id} deleted"})