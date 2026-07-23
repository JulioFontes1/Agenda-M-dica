from app.models.user import User


def test_create_user(app):
    user = User(
        name="Carlos",
        email="carlos@email.com"
    )

    assert user.name == "Carlos"
    assert user.email == "carlos@email.com"