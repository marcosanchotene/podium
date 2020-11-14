import pytest

from actions.ask_question import AskQuestion
from actions.login import Login
from actions.play_video import PlayVideo
from actions.sign_up import SignUp
from actions.watch_demo import WatchDemo
from entities.user import User


class TestWatchDemo:

    def test_should_watch_demo_from_menu_with_valid_details(self, chrome):
        browser = chrome
        test_user = User()
        watch_demo = WatchDemo(browser)
        watch_demo.from_home_page_menu(test_user)


class TestLogin:

    def test_login_forgot_password_without_email_should_display_email_or_mobile_required_message(self, chrome):
        browser = chrome
        test_user = User(email="")
        login = Login(browser)
        with pytest.raises(AssertionError):
            login.forgot_password_with_email(test_user)

    def test_login_forgot_password_without_mobile_should_display_email_or_mobile_required_message(self, chrome):
        browser = chrome
        test_user = User(mobile="")
        login = Login(browser)
        with pytest.raises(AssertionError):
            login.forgot_password_with_mobile(test_user)


class TestAskQuestion:

    def test_filling_details_on_ask_question_icon_should_enable_send_button(self, chrome):
        browser = chrome
        test_user = User()
        ask_question = AskQuestion(browser)
        ask_question.from_home_page(test_user, message="Hello. This is a test message. Please ignore.")


class TestSignUp:

    @pytest.fixture(scope="function")
    def sign_up_setup(self, chrome):
        browser = chrome
        test_user = User()
        sign_up = SignUp(browser)
        return test_user, sign_up

    def test_sign_up_with_first_get_started_link(self, sign_up_setup):
        test_user, sign_up = sign_up_setup
        sign_up.sign_up_with_first_link(test_user)

    def test_sign_up_with_second_get_started_link(self, sign_up_setup):
        test_user, sign_up = sign_up_setup
        sign_up.sign_up_with_second_link(test_user)

    def test_sign_up_with_third_get_started_link(self, sign_up_setup):
        test_user, sign_up = sign_up_setup
        sign_up.sign_up_with_third_link(test_user)


class TestVideos:

    def test_video_should_be_enabled_when_clicked(self, chrome):
        browser = chrome
        play_video = PlayVideo(browser)
        play_video.on_home_page()
