from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.project_list_page import ProjectListPage


class AdminPage:
    add_project_button = (By.CSS_SELECTOR, 'li:first-of-type a.button_link')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open_new_project_creating_page(self):
        self.browser.find_element(*self.add_project_button).click()
        return ProjectListPage(self.browser)
