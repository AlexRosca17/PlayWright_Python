from typing import Any

from helper.elements_methods import ElementsMethods
from playwright.sync_api import Page

from web_table_elements.webtable_locators import WebTableLocators


class WebTablePage(ElementsMethods, WebTableLocators):

    

    def __init__(self, page: Page):
        super().__init__(page)

    def click_add_button(self):
        self.click_element(self.ADDBUTTON)
    
    def click_delete_button(self):
        self.click_element(self.DELETE_BUTTON)

    def click_submit_button(self):
        self.click_element(self.SUBMIT)    
    
    def fill_firstname(self, text: str):
        self.fill_element(self.FIRSTNAME, text)

    def fill_lastname(self, text: str):
        self.fill_element(self.LASTNAME, text)

    def fill_email(self, text: str):
        self.fill_element(self.EMAIL, text)

    def fill_age(self, text: str):
        self.fill_element(self.AGE, text)

    def fill_salary(self, text: str):
        self.fill_element(self.SALARY, text)

    def fill_department(self, text: str):
        self.fill_element(self.DEPARTMENT, text)

    
    def get_firstname_cell(self) -> str:
        return self.page.locator(self.FIRSTNAME_CELL).inner_text()

    def get_lastname_cell(self) -> str:
        return self.page.locator(self.LASTNAME_CELL).inner_text()

    def get_email_cell(self) -> str:
        return self.page.locator(self.EMAIL_CELL).inner_text()

    def get_age_cell(self) -> str:
        return self.page.locator(self.AGE_CELL).inner_text()

    def get_salary_cell(self) -> str:
        return self.page.locator(self.SALARY_CELL).inner_text()

    def get_department_cell(self) -> str:
        return self.page.locator(self.DEPARTMENT_CELL).inner_text()
    
    def fill_all_fields(self, data: dict[str, Any]):
        self.fill_firstname(data["first_name"])
        self.fill_lastname(data["last_name"])
        self.fill_email(data["email"])
        self.fill_age(data["age"])
        self.fill_salary(data["salary"])
        self.fill_department(data["department"])
        self.click_submit_button()

    def verify_cell_values(self, data: dict[str, Any]):
        assert self.get_firstname_cell() == data["first_name"]
        assert self.get_lastname_cell() == data["last_name"]
        assert self.get_email_cell() == data["email"]
        assert self.get_age_cell() == data["age"]
        assert self.get_salary_cell() == data["salary"]
        assert self.get_department_cell() == data["department"]
