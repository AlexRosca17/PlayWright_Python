from typing import Any
from helper.elements_methods import ElementsMethods
from playwright.sync_api import Page
from locators.webtable_locators import WebTableLocators

class WebTablePage(ElementsMethods, WebTableLocators):

    def __init__(self, page: Page):
        super().__init__(page)

    def click_add_button(self):
        self.click_element(self.ADDBUTTON)
    
    def click_delete_button(self):
        self.click_element(self.DELETE_BUTTON)

    def click_submit_button(self):
        self.click_element(self.SUBMIT)    
    
    def __fill_firstname__(self, text: str):
        self.fill_element(self.FIRSTNAME, text)

    def __fill_lastname__(self, text: str):
        self.fill_element(self.LASTNAME, text)

    def __fill_email__(self, text: str):
        self.fill_element(self.EMAIL, text)

    def __fill_age__(self, text: str):
        self.fill_element(self.AGE, text)

    def __fill_salary__(self, text: str):
        self.fill_element(self.SALARY, text)

    def __fill_department__(self, text: str):
        self.fill_element(self.DEPARTMENT, text)

    def __get_firstname_cell__(self) -> str:
        return self.page.locator(self.FIRSTNAME_CELL).inner_text()

    def __get_lastname_cell__(self) -> str:
        return self.page.locator(self.LASTNAME_CELL).inner_text()

    def __get_email_cell__(self) -> str:
        return self.page.locator(self.EMAIL_CELL).inner_text()

    def __get_age_cell__(self) -> str:
        return self.page.locator(self.AGE_CELL).inner_text()

    def __get_salary_cell__(self) -> str:
        return self.page.locator(self.SALARY_CELL).inner_text()

    def __get_department_cell__(self) -> str:
        return self.page.locator(self.DEPARTMENT_CELL).inner_text()
    
    def fill_all_fields(self, data: dict[str, Any]):
        self.__fill_firstname__(data["first_name"])
        self.__fill_lastname__(data["last_name"])
        self.__fill_email__(data["email"])
        self.__fill_age__(data["age"])
        self.__fill_salary__(data["salary"])
        self.__fill_department__(data["department"])
        self.click_submit_button()

    def verify_cell_values(self, data: dict[str, Any]):
        assert self.__get_firstname_cell__() == data["first_name"]
        assert self.__get_lastname_cell__() == data["last_name"]
        assert self.__get_email_cell__() == data["email"]
        assert self.__get_age_cell__() == data["age"]
        assert self.__get_salary_cell__() == data["salary"]
        assert self.__get_department_cell__() == data["department"]
