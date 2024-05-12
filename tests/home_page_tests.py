from urllib.parse import urljoin
from demoqa_qa.steps.home_page_steps import HomePageSteps
from urls import urls


class TestHomePage:

    def test_text_box(self, home_page_steps: HomePageSteps):
       home_page_steps.open_page(urljoin(urls.demoqa_host, urls.TEXT_BOX))

