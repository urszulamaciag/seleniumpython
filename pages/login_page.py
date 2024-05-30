from selenium.webdriver.common.by import By


class LoginPage:
    url = 'http://demo.testarena.pl/zaloguj'

    email_input = (By.CSS_SELECTOR, '#email')
    password_input = (By.CSS_SELECTOR, '#password')
    login_button = (By.CSS_SELECTOR, '#login')

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get(self.url)
        return self

    def attempt_login(self, email, password):
        self.browser.find_element(*self.email_input).send_keys(email)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.login_button).click()
