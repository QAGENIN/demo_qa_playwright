from playwright.sync_api import Page

from demoqa_qa.pages.base_page import BasePage


class HomePage(BasePage):
    page_title = '.text-center'
    full_name = '#userName'
    email = '#userEmail'
    current_address = '#currentAddress'
    permanent_address = '#permanentAddress'
    submit = '#submit'