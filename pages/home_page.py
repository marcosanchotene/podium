from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.ask_question_component import AskQuestionComponent
from pages.login.auth_page import AuthPage
from pages.sign_up.sign_up_page import SignUpPage
from pages.watch_demo.watch_now_page import WatchNowPage


class HomePage:
    HOME_URL = 'https://www.podium.com/'
    SLIDER_WATCH_NOW_BUTTON_CSS = (By.CSS_SELECTOR, "#primary.primary-button.play-icon.desk-btn")
    MENU_WATCH_NOW_BUTTON_CSS = (By.CSS_SELECTOR, ".menu a.blue-box")
    LOGIN_LINK_CSS = (By.CSS_SELECTOR, "a[href='https://app.podium.com/']")
    PODIUM_MODAL_IFRAME_ID = (By.ID, "podium-modal")
    PODIUM_BUBBLE_ID = (By.ID, "podium-bubble")
    BUTTON_BUBBLE_CSS = (By.CSS_SELECTOR, "button.ContactBubble__Bubble")
    VIDEO1_CARD_ID = (By.ID, "video-1-img")
    VIDEO1_POPOVER_ID = (By.ID, "wistia-vvd1bukwgt-1_popover_container")
    GET_STARTED_LINKS_ID = (By.ID, "f-cta-1")
    VIDEO1_CLOSE_BUTTON_ID = (By.ID, "wistia-vvd1bukwgt-1_popover_popover_close_button")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.HOME_URL)
        self.wait = WebDriverWait(self.driver, 5)

    def click_slider_watch_now_button(self):
        self.driver.find_element(*self.SLIDER_WATCH_NOW_BUTTON_CSS).click()
        return WatchNowPage(self.driver)

    def click_menu_watch_now_button(self):
        self.driver.find_element(*self.MENU_WATCH_NOW_BUTTON_CSS).click()
        return WatchNowPage(self.driver)

    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK_CSS).click()
        return AuthPage(self.driver)

    def click_ask_question_bubble_icon(self):
        self.wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(self.PODIUM_BUBBLE_ID))
        self.driver.find_element(*self.BUTTON_BUBBLE_CSS).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*self.PODIUM_MODAL_IFRAME_ID))
        return AskQuestionComponent(self.driver)

    def click_video1_card(self):
        self.driver.find_element(*self.VIDEO1_CARD_ID).click()

    def video1_pop_over_is_enabled(self):
        video1_pop_over = self.wait.until(expected_conditions.visibility_of_element_located(self.VIDEO1_POPOVER_ID))
        return video1_pop_over.is_displayed()

    def click_get_started_link(self, index):
        get_started_links = self.driver.find_elements(*self.GET_STARTED_LINKS_ID)
        get_started_links[index].click()
        return SignUpPage(self.driver)

    def close_video1(self):
        self.driver.find_element(*self.VIDEO1_CLOSE_BUTTON_ID).click()
