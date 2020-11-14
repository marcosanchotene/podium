from selenium.webdriver.common.by import By


class AskQuestionComponent:
    NAME_INPUT_ID = (By.ID, "Name")
    MOBILE_INPUT_ID = (By.ID, "Mobile Phone")
    MESSAGE_INPUT_ID = (By.ID, "Message")
    VALID_SEND_BUTTON_CSS = (By.CSS_SELECTOR, "#ComposeMessage .SendButton.SendButton--valid")

    def __init__(self, driver):
        self.driver = driver

    def type_name(self, name):
        self.driver.find_element(*self.NAME_INPUT_ID).send_keys(name)

    def type_mobile(self, mobile):
        self.driver.find_element(*self.MOBILE_INPUT_ID).send_keys(mobile)

    def type_message(self, message):
        self.driver.find_element(*self.MESSAGE_INPUT_ID).send_keys(message)

    def send_button_is_enabled(self):
        result = False
        if self.driver.find_elements(*self.VALID_SEND_BUTTON_CSS):
            result = True
        return result
