import sys
import os
from venv import logger
import pytest
from typing import Generator
from playwright.sync_api import sync_playwright, Page

from helper.constants import Constants

sys.path.insert(0, os.path.dirname(__file__))

def pytest_sessionstart():
    log_file = os.path.join(os.path.dirname(__file__), "test_run.log")
    open(log_file, "w").close()

@pytest.fixture
def browser_page() -> Generator[Page, None, None]:
    is_ci = os.getenv("CI") == "true"
    pw = sync_playwright().start()
    browser = pw.chromium.launch(
        headless=is_ci,
        args=[] if is_ci else ["--start-maximized"]
    )
    page = browser.new_page()
    page.goto(Constants.BASE_URL)
    logger.info(f"Navigated to {Constants.BASE_URL}")
    yield page
    browser.close()
    pw.stop()
