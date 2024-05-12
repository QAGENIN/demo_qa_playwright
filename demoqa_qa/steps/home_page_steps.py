from urllib.parse import urljoin

from hamcrest import assert_that, equal_to
from playwright.sync_api import Page
from playwright.sync_api import expect
from demoqa_qa.constants import TEXT_BOX_TITLE
from demoqa_qa.pages.home_page import HomePage
from urls import urls


class HomePageSteps:
    def __init__(self, browser: Page):
        self.browser = browser
        self.home_page = HomePage()

    def check_title(self, locator, text):
        expect(self.browser.locator(locator)).to_have_text(text)

    def open_text_box(self):
        self.browser.goto(urljoin(urls.demoqa_host, urls.TEXT_BOX), timeout=50000)
        self.check_title(self.home_page.text_box_title, TEXT_BOX_TITLE)




