from pages.home_page import HomePage


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def forgot_password_with_email(self, user):
        self.forgot_password(user, "email")

    def forgot_password_with_mobile(self, user):
        self.forgot_password(user, "mobile")

    def forgot_password(self, user, personal_detail):
        auth_page = self.home_page.click_login_link()
        request_code_page = auth_page.click_forgot_password_link()
        if personal_detail == "email":
            request_code_page.login_common.type_email(user.email)
        elif personal_detail == "mobile":
            request_code_page.login_common.type_mobile(user.mobile)
        request_code_page.click_send_code_button()
        assert not request_code_page.login_common.email_or_mobile_required_error_message_is_displayed()
