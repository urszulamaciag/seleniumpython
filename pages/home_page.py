from selenium.webdriver.common.by import By


class HomePage:
    user_email = (By.CSS_SELECTOR, ".user-info small")

    def __init__(self, browser):
        self.browser = browser

    def get_current_user_email(self):
        return self.browser.find_element(*self.user_email).text
