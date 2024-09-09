import time
import pytest
from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import OneRecipePage
from page_models.page_navigator_model import MenuMain
from page_models.page_user_model import LoginPage, RegistrationPage
from tests.teszt_data_s import TD_REGISTER


class TestFavouriteRecipe:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.fav= OneRecipePage(browser=self.browser)
        self.menu = MenuMain(browser=self.browser)
        self.login = LoginPage(browser=self.browser)
        self.reg = RegistrationPage(browser=self.browser)
        self.fav.open()
        #self.fav.browser.maximize_window()
        self.fav.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    @pytest.mark.parametrize("email, name, pwd", TD_REGISTER)
    def test_register_user(self, email, name, pwd):
        self.menu.main_menu().click()
        time.sleep(1)
        self.menu.menu_item_profile().click()
        time.sleep(1)
        self.login.button_sign_up()
        time.sleep(1)
        self.reg.input_email().send_keys(email)
        self.reg.input_name().send_keys(name)
        self.reg.input_pwd().send_keys(pwd)
        self.reg.submit_btn().click()
        time.sleep(2)
        assert "authentication" in self.browser.current_url
