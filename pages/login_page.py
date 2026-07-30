from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    """Page Object for SauceDemo Login Page."""
    
    URL = "https://www.saucedemo.com"
    
    # Selectors
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    PRODUCTS_TITLE = ".title"

    def __init__(self, page: Page):
        super().__init__(page)

    def load(self) -> None:
        self.navigate(self.URL)

    def login(self, username: str, password: str) -> None:
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.PRODUCTS_TITLE)
