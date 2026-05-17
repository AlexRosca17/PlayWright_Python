import os
from playwright.sync_api import sync_playwright
from helper.logger import get_logger

logger = get_logger(__name__)

TRACES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "traces")


class ShareData:

    def setup_method(self, method: object):
        self.test_name = getattr(method, '__name__', str(method))
        logger.info("=" * 60)
        logger.info(f"START TEST: {self.test_name}")
        logger.info("=" * 60)
        logger.info("Starting browser")
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            
            headless=True,
            args=["--start-maximized"]
        )

        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)

        self.page = self.context.new_page()
        self.page.set_viewport_size({"width": 1920, "height": 1080})

        self.page.goto("https://demoqa.com")
        logger.info("Navigated to https://demoqa.com")

    def teardown_method(self):
        logger.info("Closing browser")
        os.makedirs(TRACES_DIR, exist_ok=True)
        self.context.tracing.stop(path=os.path.join(TRACES_DIR, f"{self.test_name}.zip"))
        self.context.close()
        self.browser.close()
        self.playwright.stop()
        logger.info(f"END TEST: {self.test_name}")
        logger.info("=" * 60)
