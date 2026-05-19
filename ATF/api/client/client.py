import requests
from typing import Any
from helper.logger import get_logger
from helper.constants import Constants

logger = get_logger(__name__)

BASE_URL = Constants.BASE_URL
AUTHORIZATION_TYPE = "Bearer "
HEADERS = {"Content-Type": "application/json"}

class Client:

    def post(self, body: dict[str, Any], endpoint: str, token: str | None = None) -> requests.Response:
        url = BASE_URL + endpoint
        if token:
            header = AUTHORIZATION_TYPE + token
            response = requests.post(url, json=body, headers={**HEADERS, "Authorization": header})
        else:
            response = requests.post(url, json=body, headers=HEADERS)
        return response
    
    def get(self, endpoint: str) -> requests.Response:
        url = BASE_URL + endpoint
        response = requests.get(url, headers=HEADERS)
        return response
    
    def put(self, body: dict[str, Any], endpoint: str) -> requests.Response:
        url = BASE_URL + endpoint
        response = requests.put(url, json=body, headers=HEADERS)
        return response
    
    def delete(self, endpoint: str) -> requests.Response:
        url = BASE_URL + endpoint
        response = requests.delete(url, headers=HEADERS)
        return response
