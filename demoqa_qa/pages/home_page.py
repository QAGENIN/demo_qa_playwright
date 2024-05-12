from playwright.sync_api import Page

from demoqa_qa.pages.base_page import BasePage


class HomePage(BasePage):
    page_title = '.text-center'

