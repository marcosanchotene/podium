from pages.home_page import HomePage


class PlayVideo:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def on_home_page(self):
        self.home_page.click_video1_card()
        assert self.home_page.video1_pop_over_is_enabled()
        self.home_page.close_video1()
