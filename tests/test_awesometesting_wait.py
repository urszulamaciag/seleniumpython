import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_post_count():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com')

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')

    # Asercja że lista ma 4 elementy
    assert titles.__len__() == 4

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_after_search():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com')

    # Inicjalizacja searchbara i przycisku search
    searchbar = browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
    search_button = browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')

    # Szukanie
    searchbar.send_keys('cypress')
    search_button.click()

    # Czekanie na stronę
    # grey_status_bar to Pythonowy tuple https://www.w3schools.com/python/python_tuples.asp
    wait = WebDriverWait(browser, 10)
    grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(EC.visibility_of_element_located(grey_status_bar))

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')

    # Asercja że lista ma 3 elementy
    assert titles.__len__() == 3

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_on_cypress_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com')

    # Inicjalizacja elementu z labelką
    cypress_label = browser.find_element(By.LINK_TEXT, 'Cypress')

    # Kliknięcie na labelkę
    cypress_label.click()

    # Czekanie na stronę
    # grey_status_bar to Pythonowy tuple https://www.w3schools.com/python/python_tuples.asp
    wait = WebDriverWait(browser, 10)
    grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(EC.visibility_of_element_located(grey_status_bar))

    # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')

    # Asercja że lista ma 1 element
    assert titles.__len__() == 1

    # Zamknięcie przeglądarki
    browser.quit()
