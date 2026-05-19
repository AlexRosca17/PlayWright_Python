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
            logger.info(f"Making POST request to {url} with body: {body} and header: {header}")
            response = requests.post(url, json=body, headers={**HEADERS, "Authorization": header})
            logger.info(f"Received response with status code: {response.status_code} and body: {response.json()}")
        else:
            response = requests.post(url, json=body, headers=HEADERS)
            logger.info(f"Making POST request to {url} with body: {body} and header: {HEADERS}")
            logger.info(f"Received response with status code: {response.status_code} and body: {response.json()}")
        return response
    
    def get(self, endpoint: str) -> requests.Response:
        url = BASE_URL + endpoint
        response = requests.get(url, headers=HEADERS)
        logger.info(f"Making GET request to {url} with header: {HEADERS}")
        logger.info(f"Received response with status code: {response.status_code} and body: {response.json()}")
        return response
    
    def put(self, body: dict[str, Any], endpoint: str) -> requests.Response:
        url = BASE_URL + endpoint
        response = requests.put(url, json=body, headers=HEADERS)
        logger.info(f"Making PUT request to {url} with body: {body} and header: {HEADERS}")
        logger.info(f"Received response with status code: {response.status_code} and body: {response.json()}")
        return response
    
    def delete(self, endpoint: str) -> requests.Response:
        url = BASE_URL + endpoint
        response = requests.delete(url, headers=HEADERS)
        logger.info(f"Making DELETE request to {url} with header: {HEADERS}")
        logger.info(f"Received response with status code: {response.status_code} and body: {response.json()}")
        return response
