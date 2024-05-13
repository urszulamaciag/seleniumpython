import time
from selenium.webdriver import Chrome

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)

    # Otwarcie strony duckduckgo
    browser.get('https://duckduckgo.com')

    # Znalezienie paska wyszukiwania
    browser.find_element(By.CSS_SELECTOR, '#searchbox_input').send_keys('4testers')

    # Znalezienie guzika wyszukiwania (lupki)
    browser.find_element(By.CSS_SELECTOR, '[aria-label=Search]').click()

    # Sprawdzamy że znaleleźliśmy nasz kurs w wynikach wyszukiwania
    title_elements = browser.find_elements(By.CSS_SELECTOR, '[data-testid=result-title-a] span')

    # Zamknięcie przeglądarki
    time.sleep(2)
    assert check_text_presence(title_elements, '4_testers Automaty')
    browser.quit()


def test_searching_in_bing():
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.get('https://bing.com')

    search_input = browser.find_element(By.CSS_SELECTOR, '#sb_form_q')
    search_input.send_keys('4testers')
    search_input.submit()

    time.sleep(3)
    title_elements = browser.find_elements(By.CSS_SELECTOR, 'h2 a')
    assert check_text_presence(title_elements, '4_testers Automaty')
    browser.quit()


def check_text_presence(elements, text):
    for element in elements:
        if text in element.text:
            return True
    return False
