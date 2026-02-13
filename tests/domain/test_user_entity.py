from app.domain.accounts.entities import User
from app.domain.accounts.exceptions import InvalidEmailError


def test_create_user_with_valid_email():
    user = User.create(email="test@example.com", full_name="Test User")
    assert user.email == "test@example.com"
    assert user.full_name == "Test User"
    assert user.is_active is True


def test_create_user_with_invalid_email_raises():
    try:
        User.create(email="invalid-email", full_name="Test User")
    except InvalidEmailError as exc:
        assert "@" in exc.message or exc.code == "invalid_email"
    else:
        assert False, "Expected InvalidEmailError to be raised"

