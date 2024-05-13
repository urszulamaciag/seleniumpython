from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.chrome import chrome_browser


def test_successful_login(chrome_browser):
    administrator_email = 'administrator@testarena.pl'
    chrome_browser.set_window_size(1920, 1080)
    chrome_browser.get('http://demo.testarena.pl/zaloguj')

    chrome_browser.find_element(By.CSS_SELECTOR, '#email').send_keys(administrator_email)
    chrome_browser.find_element(By.CSS_SELECTOR, '#password').send_keys('sumXQQ72$L')
    chrome_browser.find_element(By.CSS_SELECTOR, '#login').click()

    user_email = chrome_browser.find_element(By.CSS_SELECTOR, ".user-info small")
    assert administrator_email == user_email.text

