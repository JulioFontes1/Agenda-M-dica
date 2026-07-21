from flask import Blueprint
from flask_login import login_required
from flask_login import current_user

agenda = Blueprint(
    "agenda",
    __name__
)

@agenda.route("/")
@login_required
def home():
    return "Agenda Médica"