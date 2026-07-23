from werkzeug.security import generate_password_hash

from app.database import db
from app.models.user import User


def test_login(client, app):
    with app.app_context():
        user = User(
            name="John",
            email="john@email.teste",
            password=generate_password_hash("teste1234")
        )

        db.session.add(user)
        db.session.commit()

    response = client.post(
        "/login",
        data={
            "email": "john@email.teste",
            "password": "teste1234"
        },
        follow_redirects=True
    )

    assert response.status_code == 200