from pages.home_page import HomePage


class SignUp:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def sign_up_with_first_link(self, user):
        self.sign_up(user, index=0)

    def sign_up_with_second_link(self, user):
        self.sign_up(user, index=1)

    def sign_up_with_third_link(self, user):
        self.sign_up(user, index=2)

    def sign_up(self, user, index):
        sign_up_page = self.home_page.click_get_started_link(index)
        sign_up_page.type_first_name(user.first_name)
        sign_up_page.type_last_name(user.last_name)
        sign_up_page.type_email(user.email)
        sign_up_page.type_mobile(user.mobile)
        sign_up_page.type_business_name(user.company)
