from selenium.webdriver import Edge

import pytest
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def edge_browser():
    service = Service(EdgeChromiumDriverManager().install())
    browser = Edge(service=service)
    yield browser
    browser.quit()
