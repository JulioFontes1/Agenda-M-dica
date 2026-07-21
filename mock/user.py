from app.app import app
from app.database import db
from app.models.user import User
from werkzeug.security import generate_password_hash

with app.app_context():
    user = User(
        name="Admin",
        email="admin@email.teste",
        password=generate_password_hash("senha_teste")
    )

    db.session.add(user)
    db.session.commit()

    print("Usuário criado!")