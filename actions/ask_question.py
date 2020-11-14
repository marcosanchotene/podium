from pages.home_page import HomePage


class AskQuestion:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def from_home_page(self, user, message):
        ask_question_component = self.home_page.click_ask_question_bubble_icon()
        ask_question_component.type_name(user.full_name)
        ask_question_component.type_mobile(user.mobile)
        ask_question_component.type_message(message)
        assert ask_question_component.send_button_is_enabled()
