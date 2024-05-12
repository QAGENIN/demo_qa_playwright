from urllib.parse import urljoin

from playwright.sync_api import Page, sync_playwright
from demoqa_qa.steps.home_page_steps import HomePageSteps
from urls import urls


class TestHomePage:

    def test_text_box(self, home_page_steps: HomePageSteps):
       home_page_steps.open_text_box()

