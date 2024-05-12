import pytest
from playwright.async_api import Page
from playwright.sync_api import sync_playwright

from demoqa_qa.steps.home_page_steps import HomePageSteps


@pytest.fixture
def home_page_steps(browser: Page) -> HomePageSteps:
    return HomePageSteps(browser)


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()