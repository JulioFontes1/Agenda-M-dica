from app import create_app
from .database import db
from flask_migrate import Migrate
from app.models.appointment import Appointment

from flask_login import login_required
from app.utils import get_string

app = create_app()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)