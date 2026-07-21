from app.app import app
from app.database import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

with app.app_context():
    senha = "senha_tste"
    usuario = db.session.get(User, 1)

    if check_password_hash(usuario.password, senha):
        print("OK")
    else:
        print("Nop")
