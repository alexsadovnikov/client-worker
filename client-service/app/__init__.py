from flask import Blueprint

from app.routes.projects import projects_bp
from app.routes.tasks import tasks_bp
from app.routes.users import users_bp
from app.routes.timesheets import timesheets_bp
from app.routes.expenses import expenses_bp
from app.routes.analytics import analytics_bp
from app.routes.financials import financials_bp

api = Blueprint("api", __name__)  # ⬅️ нет url_prefix

api.register_blueprint(projects_bp, url_prefix="/projects")
api.register_blueprint(tasks_bp, url_prefix="/tasks")
api.register_blueprint(users_bp, url_prefix="/users")
api.register_blueprint(timesheets_bp, url_prefix="/timesheets")
api.register_blueprint(expenses_bp, url_prefix="/expenses")
api.register_blueprint(analytics_bp, url_prefix="/analytics")
api.register_blueprint(financials_bp, url_prefix="/financials")
