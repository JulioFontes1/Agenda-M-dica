from flask import Flask
from app.models.user import User
from flask_login import LoginManager

from .routes.auth import auth
from .routes.agenda import agenda
from .routes.api import api


from .database import db

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dapfdafdasgndsajmdavndgasda"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///agenda.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(auth)
    app.register_blueprint(agenda)
    app.register_blueprint(api)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.init_app(app)

    return app