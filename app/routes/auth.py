from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from app.models.user import User

auth = Blueprint(
    "auth", __name__
)

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
    
        flash(
                "Email ou senha inválidos.",
                "error"
            )
    
    return render_template(
        "login.html"
    )

@auth.route("/logout")
def logout():

    logout_user()

    return redirect("/login")