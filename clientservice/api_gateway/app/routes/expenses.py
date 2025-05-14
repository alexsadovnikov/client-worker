from flask import Blueprint, jsonify, request
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from flask_smorest import Blueprint as SmorestBlueprint

expenses_bp = SmorestBlueprint("expenses", __name__, url_prefix="/expenses")

@expenses_bp.route("/", methods=["GET"])
@expenses_bp.response(200, description="Список расходов")
def get_expenses():
    return []

@expenses_bp.route("/", methods=["POST"])
@expenses_bp.arguments(ExpenseCreate)
@expenses_bp.response(201, description="Создан расход")
def create_expense(data):
    return data