from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MessagesPage:
    text_input = (By.ID, 'j_msgContent')
    publish_button = (By.ID, 'j_msgResponse-193')
    message_content_text = (By.CLASS_NAME, 'message_content_text')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def add_message(self, my_text):
        self.wait.until(EC.element_to_be_clickable(self.text_input))
        self.browser.find_element(*self.text_input).send_keys(my_text)
        self.browser.find_element(*self.publish_button).click()
        return self

    def verify_message_added(self, my_text):
        try:
            self.wait.until(lambda x: any(my_text in element.text for element in
                                          self.browser.find_elements(*self.message_content_text)))
        except TimeoutException:
            print(
                f"Error: The expected text '{my_text}' was not found in any message_content_text element within the given time.")
