import pytest

def test_successful_login(login_page):
    """Verify login with valid credentials."""
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()

def test_invalid_login(login_page):
    """Verify login failure with invalid password."""
    login_page.login("standard_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error_message()
