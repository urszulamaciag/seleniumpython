from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectCreatingPage:
    project_name_input = (By.ID, 'name')
    project_suffix_input = (By.ID, 'prefix')
    project_save_button = (By.ID, 'save')
    back_to_project_list_button = (By.CLASS_NAME, 'icon_puzzle_alt')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def add_project(self, my_project_name, my_project_suffix):
        self.wait.until(EC.element_to_be_clickable(self.project_name_input))
        self.browser.find_element(*self.project_name_input).send_keys(my_project_name)
        self.browser.find_element(*self.project_suffix_input).send_keys(my_project_suffix)
        self.browser.find_element(*self.project_save_button).click()
        return self

    def back_to_project_list(self):
        self.browser.find_element(*self.back_to_project_list_button).click()
