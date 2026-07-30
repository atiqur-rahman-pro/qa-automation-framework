from playwright.sync_api import Page, Locator

class BasePage:
    """Base Page Object containing common web interaction methods."""
    
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, selector: str) -> None:
        self.page.click(selector)

    def fill(self, selector: str, text: str) -> None:
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
