from selenium.webdriver.common.by import By


class SignUpPage:
    FIRST_NAME_INPUT_ID = (By.ID, "first-name")
    LAST_NAME_INPUT_ID = (By.ID, "last-name")
    EMAIL_INPUT_ID = (By.ID, "email")
    MOBILE_INPUT_ID = (By.ID, "phone")
    BUSINESS_NAME_INPUT_ID = (By.ID, "business-name")

    def __init__(self, driver):
        self.driver = driver

    def type_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT_ID).send_keys(first_name)

    def type_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT_ID).send_keys(last_name)

    def type_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT_ID).send_keys(email)

    def type_mobile(self, mobile):
        self.driver.find_element(*self.MOBILE_INPUT_ID).send_keys(mobile)

    def type_business_name(self, business_name):
        self.driver.find_element(*self.BUSINESS_NAME_INPUT_ID).send_keys(business_name)
