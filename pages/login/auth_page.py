from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login.request_code_page import RequestCodePage


class AuthPage:
    FORGOT_PASSWORD_ID = (By.ID, "forgotPasswordText")

    def __init__(self, driver):
        self.driver = driver

    def click_forgot_password_link(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.FORGOT_PASSWORD_ID)).click()
        return RequestCodePage(self.driver)
