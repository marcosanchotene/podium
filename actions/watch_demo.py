from pages.home_page import HomePage


class WatchDemo:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def from_home_page_slider(self, user):
        watch_now_page = self.home_page.click_slider_watch_now_button()
        self.type_user_details_to_watch_demo(watch_now_page, user)

    def from_home_page_menu(self, user):
        watch_now_page = self.home_page.click_menu_watch_now_button()
        self.type_user_details_to_watch_demo(watch_now_page, user)

    @staticmethod
    def type_user_details_to_watch_demo(watch_now_page, user):
        watch_now_page.type_email(user.email)
        watch_now_page.click_watch_demo_button()
        watch_now_page.type_first_name(user.first_name)
        watch_now_page.type_last_name(user.last_name)
        watch_now_page.type_company(user.company)
        watch_now_page.type_mobile(user.mobile)
        assert not watch_now_page.valid_email_error_message_is_displayed()
