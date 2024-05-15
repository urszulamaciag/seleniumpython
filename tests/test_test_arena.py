import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages.home_page import HomePage

administrator_email = 'administrator@testarena.pl'


def test_successful_login(browser):
    home_page = HomePage(browser)
    user_email = home_page.get_current_user_email()
    assert administrator_email == user_email


def test_add_message(browser):
    browser.find_element(By.CLASS_NAME, 'icon_mail').click()
    wait = WebDriverWait(browser, 10)
    text_input = (By.ID, 'j_msgContent')
    wait.until(EC.element_to_be_clickable(text_input))
    my_text = generate_random_string(10)
    browser.find_element(*text_input).send_keys(my_text)
    browser.find_element(By.ID, 'j_msgResponse-193').click()
    wait.until(lambda x: browser.find_elements(By.CLASS_NAME, 'message_content_text')[-1].text == my_text)
    assert browser.find_elements(By.CLASS_NAME, 'message_content_text')[-1].text == my_text


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
