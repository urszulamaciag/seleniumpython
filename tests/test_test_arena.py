import random
import string

from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages.home_page import HomePage
from pages.messages_page import MessagesPage

administrator_email = 'administrator@testarena.pl'


def test_successful_login(browser):
    home_page = HomePage(browser)
    user_email = home_page.get_current_user_email()
    assert administrator_email == user_email


def test_add_message(browser):
    my_text = generate_random_string(10)

    home_page = HomePage(browser)
    home_page.click_mail_icon()

    messages_page = MessagesPage(browser)
    messages_page.add_message(my_text)
    messages_page.verify_message_added(my_text)


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
