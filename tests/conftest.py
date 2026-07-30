import pytest
import os
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def login_page(page: Page):
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.load()
    return login

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Takes a screenshot automatically when a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
