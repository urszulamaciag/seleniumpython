from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectListPage:
    project_suffix = (By.CLASS_NAME, 't_number')
    project_name_listed = (By.CSS_SELECTOR, 'td:nth-child(1)')
    project_search_input = (By.ID, 'search')
    project_search_icon = (By.ID, 'j_searchButton')
    back_to_project_list_button = (By.CLASS_NAME, 'icon_puzzle_alt')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
    #
    # def verify_project_added(self, my_project_name):
    #     try:
    #         self.wait.until(lambda x: any(my_project_name in element.text for element in
    #                                       self.browser.find_elements(*self.project_name_listed)))
    #     except TimeoutException:
    #         print(
    #             f"Error: The expected text '{my_project_name}' was not found in any project_name_listed element within the given time.")

    def search_project_on_project_list(self, my_project_name):
        self.wait.until(EC.element_to_be_clickable(self.project_search_input))
        self.browser.find_element(*self.project_search_input).send_keys(my_project_name)
        self.browser.find_element(*self.project_search_icon).click()

    def is_project_in_list(self, my_project_name):
        project_elements = self.browser.find_elements(*self.project_name_listed)
        for element in project_elements:
            if my_project_name in element.text:
                return True
        return False
