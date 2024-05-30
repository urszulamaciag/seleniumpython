from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.admin_page import AdminPage
from pages.messages_page import MessagesPage


class HomePage:
    user_email = (By.CSS_SELECTOR, ".user-info small")
    mail_icon = (By.CLASS_NAME, 'icon_mail')
    admin_panel_icon = (By.CLASS_NAME, 'icon_tools')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def get_current_user_email(self):
        return self.browser.find_element(*self.user_email).text

    def click_mail_icon(self):
        self.browser.find_element(*self.mail_icon).click()
        return MessagesPage(self.browser)

    def open_admin_panel(self):
        self.browser.find_element(*self.admin_panel_icon).click()
        return AdminPage(self.browser)
