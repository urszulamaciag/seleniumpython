from selenium.webdriver import Firefox

import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def edge_browser():
    service = Service(GeckoDriverManager().install())
    browser = Firefox(service=service)
    yield browser
    browser.quit()
