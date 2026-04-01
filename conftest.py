import pytest
from playwright.sync_api import sync_playwright
from config.config_reader import config

@pytest.fixture(scope="session")
def page():
    with sync_playwright as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        yield page
        browser.close()