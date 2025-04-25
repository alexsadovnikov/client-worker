from app.extensions import db
from datetime import datetime

class TimeEntry(db.Model):
    __tablename__ = 'time_entries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    hours = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

    user = db.relationship('User')
    project = db.relationship('Project')
