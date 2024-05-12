from playwright.sync_api import Page
from playwright.sync_api import expect
from demoqa_qa.pages.home_page import HomePage


class HomePageSteps:
    def __init__(self, browser: Page):
        self.browser = browser
        self.home_page = HomePage()


    def open_page(self, url: str) -> None:
        self.browser.goto(url, timeout=50000)
        expect(self.browser.locator(self.home_page.page_title), 'should be visible').to_be_visible()
