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

    def filling_text_box_fields(self):
        test_text = 'Test Test'
        test_email = 'Test@Test.ru'
        self.browser.locator(self.home_page.full_name).fill(test_text)
        self.browser.locator(self.home_page.email).fill(test_email)
        self.browser.locator(self.home_page.current_address).fill(test_text)
        self.browser.locator(self.home_page.permanent_address).fill(test_text)
        self.browser.locator(self.home_page.submit).click()
        # Дописать проверку, сделать датакласс с юзером виесто констант
