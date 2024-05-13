from selenium.webdriver import Chrome

import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def chrome_browser():
    # Sekcja 1 - co wykona się przed każdym testem który korzysta z tego fixture'a
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    # Sekcja 2 - co fixture przekazuje do testów
    yield browser
    # Sekcje 3 - co wykona się po każdym teście
    browser.quit()
