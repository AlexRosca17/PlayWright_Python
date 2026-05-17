from playwright.sync_api import Page
from helper.elements_methods import ElementsMethods


class HomePage(ElementsMethods):

    ELEMENTS = "(//*[@class='card-body'])[1]"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_elements(self):
        self.click_element(self.ELEMENTS)
