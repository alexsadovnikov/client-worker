from flask import Flask
from app.routes.projects import projects_bp
from app.routes.tasks import tasks_bp
from app.routes.users import users_bp
from app.routes.timesheets import timesheets_bp
from app.routes.expenses import expenses_bp
from app.routes.analytics import analytics_bp
from app.routes.financials import financials_bp

from flasgger import Swagger
def create_app():
    app = Flask(__name__)

    # Настройка Swagger
    app.config['SWAGGER'] = {
        'title': 'ClientService API',
        'uiversion': 3
    }
    Swagger(app)

    @app.route("/")
    def index():
        return {"status": "ClientService API is running"}, 200

    # Регистрация маршрутов
    app.register_blueprint(projects_bp, url_prefix="/projects")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(timesheets_bp, url_prefix="/timesheets")
    app.register_blueprint(expenses_bp, url_prefix="/expenses")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")
    app.register_blueprint(financials_bp, url_prefix="/financials")

    return app