import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from config.config_reader import config
import allure

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page")

        if report.failed and page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name

            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"

            page.screenshot(path=screenshot_path)

            # 🔥 Attach to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )