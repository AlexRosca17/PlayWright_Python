from playwright.sync_api import Page
from helper.logger import get_logger

logger = get_logger(__name__)


class ElementsMethods:

    def __init__(self, page: Page):
        self.page = page

    def click_element(self, locator: str):
        logger.info(f"Clicking element: {locator}")
        self.page.locator(locator).click()

    def fill_element(self, locator: str, text: str):
        logger.info(f"Filling element: {locator} with value: {text}")
        self.page.locator(locator).fill(text)
