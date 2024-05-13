from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_successful_login():
    administrator_email = 'administrator@testarena.pl'
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.set_window_size(1920, 1080)
    browser.get('http://demo.testarena.pl/zaloguj')

    # Wpisanie credentiali
    browser.find_element(By.CSS_SELECTOR, '#email').send_keys(administrator_email)
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('sumXQQ72$L')
    browser.find_element(By.CSS_SELECTOR, '#login').click()

    user_email = browser.find_element(By.CSS_SELECTOR, ".user-info small")
    assert administrator_email == user_email.text

    browser.quit()

