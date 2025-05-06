from flask import Blueprint, jsonify, request
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from flasgger import swag_from

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/expenses", methods=["GET"])
@swag_from("docs/expenses/get_expenses.yml")
def get_expenses():
    return jsonify([])

@expenses_bp.route("/expenses", methods=["POST"])
@swag_from("docs/expenses/create_expenses.yml")
def create_expense():
    data = request.get_json()
    expense = ExpenseCreate(**data)
    return jsonify(expense.dict()), 201

@expenses_bp.route("/expenses/<int:expense_id>", methods=["GET"])
@swag_from("docs/expenses/get_expense_by_id.yml")
def get_expense(expense_id):
    return jsonify({"id": expense_id})

@expenses_bp.route("/expenses/<int:expense_id>", methods=["PUT"])
@swag_from("docs/expenses/update_expense.yml")
def update_expense(expense_id):
    data = request.get_json()
    expense_update = ExpenseUpdate(**data)
    return jsonify({"id": expense_id, **expense_update.dict()})

@expenses_bp.route("/expenses/<int:expense_id>", methods=["DELETE"])
@swag_from("docs/expenses/delete_expense.yml")
def delete_expense(expense_id):
    return jsonify({"message": f"Expense {expense_id} deleted"})