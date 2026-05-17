from helper.data_loader import load_test_data
from pages.common_page import CommonPage
from pages.home_page import HomePage
from pages.webtable_page import WebTablePage
from share_data.share_data import ShareData
import allure

class Test_Webtable(ShareData):

    @allure.tag("Regression")
    def test_add_new_entry(self):
        data = load_test_data("webtable_data.json", "1")
        home_page = HomePage(self.page)
        home_page.click_elements()

        common_page = CommonPage(self.page)
        common_page.click_web_tables()

        assert self.page.url == "https://demoqa.com/webtables"

        webtable_page = WebTablePage(self.page)
        webtable_page.click_add_button()
        webtable_page.fill_all_fields(data)
        webtable_page.verify_cell_values(data)

    @allure.tag("Regression")
    def test_delete_entry(self):
        home_page = HomePage(self.page)
        home_page.click_elements()

        common_page = CommonPage(self.page)
        common_page.click_web_tables()

        assert self.page.url == "https://demoqa.com/webtables"

        webtable_page = WebTablePage(self.page)
        webtable_page.click_delete_button()
        
    
