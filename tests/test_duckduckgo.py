import time

from selenium.webdriver.common.by import By
from fixtures.chrome import chrome_browser


def test_searching_in_duckduckgo(chrome_browser):
    chrome_browser.get('https://duckduckgo.com')
    chrome_browser.find_element(By.CSS_SELECTOR, '#searchbox_input').send_keys('4testers')
    chrome_browser.find_element(By.CSS_SELECTOR, '[aria-label=Search]').click()
    title_elements = chrome_browser.find_elements(By.CSS_SELECTOR, '[data-testid=result-title-a] span')

    time.sleep(2)
    assert check_text_presence(title_elements, '4_testers Automaty')


def test_searching_in_bing(chrome_browser):
    chrome_browser.get('https://bing.com')
    search_input = chrome_browser.find_element(By.CSS_SELECTOR, '#sb_form_q')
    search_input.send_keys('4testers')
    search_input.submit()
    time.sleep(3)
    title_elements = chrome_browser.find_elements(By.CSS_SELECTOR, 'h2 a')
    assert check_text_presence(title_elements, '4_testers Automaty')


def check_text_presence(elements, text):
    for element in elements:
        if text in element.text:
            return True
    return False
