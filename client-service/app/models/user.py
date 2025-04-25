from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    tasks = db.relationship('Task', back_populates='user', cascade="all, delete-orphan")
    expenses = db.relationship('ExpenseRequest', back_populates='user', cascade="all, delete-orphan")
    reports = db.relationship('Report', back_populates='user', cascade="all, delete-orphan")
    expenses = db.relationship('ExpenseRequest', back_populates='user', lazy='dynamic')