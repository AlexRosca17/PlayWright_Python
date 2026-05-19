from helper.elements_methods import ElementsMethods
from elements.login_elements.login_elements import LoginElements

class LoginPage(ElementsMethods, LoginElements):

    def __complete_username__(self, username: str):
        self.fill_element(self.USERNAME_FIELD, username)

    def __complete_password__(self, password: str):
        self.fill_element(self.PASSWORD_FIELD, password)
    
    def __click_login__(self):
        self.click_element(self.LOGIN_BUTTON)

    def verify_login_successful(self) -> bool:
        self.page.wait_for_url("**/profile")
        return self.page.url.endswith("profile")
        
    def complete_login(self, username: str, password: str):
        self.__complete_username__(username)
        self.__complete_password__(password)
        self.__click_login__()