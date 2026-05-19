
from playwright.sync_api import Page
from helper.elements_methods import ElementsMethods


class CommonPage(ElementsMethods):

    WEB_TABLES = "//*[@href='/webtables']"
    LOGIN = "//*[@id='login']"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_web_tables(self):
        self.click_element(self.WEB_TABLES)
    
    def click_login(self):
        self.click_element(self.LOGIN)