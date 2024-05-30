from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.chrome import chrome_browser


def test_searching_in_duckduckgo(chrome_browser):
    chrome_browser.get('https://duckduckgo.com')
    chrome_browser.find_element(By.CSS_SELECTOR, '#searchbox_input').send_keys('4testers')
    chrome_browser.find_element(By.CSS_SELECTOR, '[aria-label=Search]').click()
    title_selector = (By.CSS_SELECTOR, '[data-testid=result-title-a] span')
    wait = WebDriverWait(chrome_browser, 10)
    wait.until(lambda x: len(chrome_browser.find_elements(*title_selector)) == 10)
    title_elements = chrome_browser.find_elements(*title_selector)
    assert check_text_presence(title_elements, '4_testers Automaty')


def test_searching_in_bing(chrome_browser):
    chrome_browser.get('https://bing.com')
    search_input = chrome_browser.find_element(By.CSS_SELECTOR, '#sb_form_q')
    search_input.send_keys('4testers')
    search_input.submit()
    wait = WebDriverWait(chrome_browser, 10)
    title_selector = (By.CSS_SELECTOR, 'h2 a')
    wait.until(lambda x: len(chrome_browser.find_elements(*title_selector)) >= 4)
    title_elements = chrome_browser.find_elements(*title_selector)
    assert check_text_presence(title_elements, '4_testers Automaty')


def check_text_presence(elements, text):
    for element in elements:
        if text in element.text:
            return True
    return False
