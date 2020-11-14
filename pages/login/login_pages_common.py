from selenium.webdriver.common.by import By


class LoginPagesCommon:
    EMAIL_MOBILE_INPUT_ID = (By.ID, "emailOrPhoneInput")
    EMAIL_OR_MOBILE_REQUIRED_MESSAGE_CSS = (By.CSS_SELECTOR, ".sc-jTzLTM.sc-fjdhpX.feWXZn")

    def __init__(self, driver):
        self.driver = driver

    def type_email(self, email):
        self.driver.find_element(*self.EMAIL_MOBILE_INPUT_ID).send_keys(email)

    def type_mobile(self, mobile):
        self.driver.find_element(*self.EMAIL_MOBILE_INPUT_ID).send_keys(mobile)

    def email_or_mobile_required_error_message_is_displayed(self):
        result = False
        if self.driver.find_elements(*self.EMAIL_OR_MOBILE_REQUIRED_MESSAGE_CSS):
            result = True
        return result
