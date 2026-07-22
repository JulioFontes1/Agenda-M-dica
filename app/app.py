from app import create_app
from .database import db
from flask_migrate import Migrate
from app.models.user import User
from app.models.appointment import Appointment
from flask_login import LoginManager
from .routes.auth import auth
from flask_login import login_required
from .routes.agenda import agenda
from app.utils import get_string
from .routes.api import api

app = create_app()

app.register_blueprint(auth)
app.register_blueprint(agenda)
app.register_blueprint(api)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(debug=True)