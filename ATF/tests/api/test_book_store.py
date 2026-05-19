import uuid
import pytest
from playwright.sync_api import Page
from api.client.client import Client
from api.endpoints.endpoints import Endpoints
from api.response.books_add_success import BooksAddSuccess
from api.response.books_response import BooksResponse
from api.response.generate_token_success import GenerateTokenSuccessResponse
from api.response.user_response import UserResponse
from helper.data_loader import load_test_data
from pages.common_page import CommonPage
from pages.home_page import HomePage
from pages.login_page import LoginPage



class TestBookStore():
    username = f"user_{uuid.uuid4().hex[:8]}"

    @pytest.mark.xdist_group("bookstore")
    def test_book_store(self):
        client = Client()
        data_account = load_test_data("account.json", "1")
        data_account["userName"] = self.username
        
        response = client.post(body=data_account, endpoint=Endpoints.CREATE_USER)
        user = UserResponse(**response.json())
        print(user.username, user.userID, user.books)
        assert response.status_code == 201

        response_token = client.post(body=data_account, endpoint=Endpoints.GENERATE_TOKEN)
        token_response = GenerateTokenSuccessResponse(**response_token.json())
        print(token_response.token, token_response.expires, token_response.status, token_response.result)

        data_books = load_test_data("books.json", "1")
        data_books["userId"] = user.userID

        response_books = client.post(body=data_books, endpoint=Endpoints.ADDBOOKS, token=token_response.token)
        response_books_success = BooksAddSuccess(**response_books.json())
        print(response_books_success.books)

        response_get_books = client.get(Endpoints.GET_BOOKS)
        response_get_books_object = BooksResponse(**response_get_books.json())
        print(response_get_books_object.books)
    
    @pytest.mark.xdist_group("bookstore")
    def test_book_store_account_validator(self, browser_page: Page):
        home_page = HomePage(browser_page)
        home_page.click_book_store()

        common_page = CommonPage(browser_page)
        common_page.click_login()

        data_account = load_test_data("account.json", "1")
        login_page = LoginPage(browser_page)
        login_page.complete_login(self.username, data_account["password"])
        assert login_page.verify_login_successful() == True