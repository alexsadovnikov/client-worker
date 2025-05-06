from flask import Blueprint, jsonify, request
from app.schemas.financial import FinancialRecordCreate, FinancialRecordUpdate

financials_bp = Blueprint("financials", __name__)

@financials_bp.route("/financials", methods=["GET"])
def get_financials():
    return jsonify([])

@financials_bp.route("/financials", methods=["POST"])
def create_financial():
    data = request.get_json()
    financial = FinancialRecordCreate(**data)
    return jsonify(financial.dict()), 201

@financials_bp.route("/financials/<int:financial_id>", methods=["GET"])
def get_financial(financial_id):
    return jsonify({"id": financial_id})

@financials_bp.route("/financials/<int:financial_id>", methods=["PUT"])
def update_financial(financial_id):
    data = request.get_json()
    financial_update = FinancialRecordUpdate(**data)
    return jsonify({"id": financial_id, **financial_update.dict()})

@financials_bp.route("/financials/<int:financial_id>", methods=["DELETE"])
def delete_financial(financial_id):
    return jsonify({"message": f"Financial record {financial_id} deleted"})