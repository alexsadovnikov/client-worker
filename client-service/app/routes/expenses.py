from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.schemas.expense import ExpenseCreate, ExpenseOut
from app.extensions import db
from app.models.expense import Expense
from pydantic import ValidationError

expenses_bp = Blueprint("expenses", __name__)  # ⬅️ Без url_prefix!

@expenses_bp.route("/", methods=["GET"])
@swag_from({
    "responses": {
        200: {
            "description": "List of all expenses",
            "schema": {
                "type": "array",
                "items": ExpenseOut.schema()
            }
        }
    }
})
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([ExpenseOut.from_orm(e).dict() for e in expenses])


@expenses_bp.route("/", methods=["POST"])
@swag_from({
    "parameters": [{
        "name": "body",
        "in": "body",
        "required": True,
        "schema": ExpenseCreate.schema()
    }],
    "responses": {
        200: {
            "description": "Expense created",
            "schema": ExpenseOut.schema()
        }
    }
})
def create_expense():
    try:
        data = ExpenseCreate(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    expense = Expense(
        project_id=data.project_id,
        description=data.description,
        amount=data.amount,
        date=data.date
    )
    db.session.add(expense)
    db.session.commit()

    return jsonify(ExpenseOut.from_orm(expense).dict())
