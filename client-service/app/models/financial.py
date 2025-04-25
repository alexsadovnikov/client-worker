from app.extensions import db
from datetime import datetime

class ExpenseRequest(db.Model):
    __tablename__ = 'expense_requests'

    id = db.Column(db.Integer, primary_key=True)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)
    currency = db.Column(db.String(50), default='RUB')
    amount = db.Column(db.Float, nullable=False)
    reimbursable = db.Column(db.Boolean, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='expenses')
