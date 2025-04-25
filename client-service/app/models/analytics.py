from app.extensions import db
from datetime import datetime

class DashboardWidget(db.Model):
    __tablename__ = 'dashboard_widgets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    widget_type = db.Column(db.String(50), nullable=False)
    config = db.Column(db.Text)


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='reports')
