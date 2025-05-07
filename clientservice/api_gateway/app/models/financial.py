from app.db import db
from datetime import datetime

class Financial(db.Model):
    __tablename__ = 'financials'

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Financial {self.account}: {self.amount}>"