from app.db import db
from datetime import datetime

class TimeEntry(db.Model):
    __tablename__ = 'time_entries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    hours = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

    user = db.relationship('User', backref='time_entries')
    project = db.relationship('Project', backref='time_entries')