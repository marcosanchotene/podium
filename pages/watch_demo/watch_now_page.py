from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WatchNowPage:
    EMAIL_ADDRESS_ID = (By.ID, "Email")
    FIRST_NAME_ID = (By.ID, "FirstName")
    LAST_NAME_ID = (By.ID, "LastName")
    COMPANY_ID = (By.ID, "Company")
    MOBILE_ID = (By.ID, "MobilePhone")
    WATCH_DEMO_BUTTON_CSS = (By.CSS_SELECTOR, "button.mktoButton")
    VALID_EMAIL_CSS = (By.CSS_SELECTOR, "span.mktoErrorDetail")
    EMAIL_DOESNT_EXIST_ID = (By.ID, "InstructEmail")
    GROUP_INBOX_MESSAGE_ID = (By.ID, "ValidMsgEmail")

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 5)

    def type_email(self, email):
        self.wait.until(expected_conditions.element_to_be_clickable(self.EMAIL_ADDRESS_ID)).send_keys(email)

    def type_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_ID).send_keys(first_name)

    def type_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_ID).send_keys(last_name)

    def type_company(self, company):
        self.driver.find_element(*self.COMPANY_ID).send_keys(company)

    def type_mobile(self, mobile):
        self.driver.find_element(*self.MOBILE_ID).send_keys(mobile)

    def click_watch_demo_button(self):
        self.driver.find_element(*self.WATCH_DEMO_BUTTON_CSS).click()

    def valid_email_error_message_is_displayed(self):
        result = False
        if self.driver.find_elements(*self.VALID_EMAIL_CSS):
            result = True
        return result

    def group_inbox_error_message_is_displayed(self):
        result = False
        if self.driver.find_elements(*self.GROUP_INBOX_MESSAGE_ID):
            result = True
        return result

    def email_doesnt_exist_error_message_is_displayed(self):
        return self.driver.find_element(*self.EMAIL_DOESNT_EXIST_ID).is_displayed()
