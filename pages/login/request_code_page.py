from selenium.webdriver.common.by import By

from pages.login.login_pages_common import LoginPagesCommon


class RequestCodePage:
    SEND_CODE_BUTTON_ID = (By.ID, "sendCodeButton")

    def __init__(self, driver):
        self.driver = driver
        self.login_common = LoginPagesCommon(self.driver)

    def click_send_code_button(self):
        self.driver.find_element(*self.SEND_CODE_BUTTON_ID).click()
