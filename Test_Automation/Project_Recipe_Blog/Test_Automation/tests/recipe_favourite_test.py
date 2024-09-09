import time
import pytest
from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import OneRecipePage
from page_models.page_navigator_model import MenuMain
from page_models.page_user_model import LoginPage
from tests.teszt_data_s import TD_LOGIN


class TestFavouriteRecipe:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.fav= OneRecipePage(browser=self.browser)
        self.menu = MenuMain(browser=self.browser)
        self.login = LoginPage(browser=self.browser)
        self.fav.open()
        #self.fav.browser.maximize_window()
        self.fav.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    def test_favourite_recipe_as_guest(self):
        self.menu.main_menu().click()
        self.menu.menu_item_recipes().click()
        self.fav.click_recipe().click()
        self.fav.favourite_btn().click()
        assert "authentication" in self.browser.current_url

    @pytest.mark.parametrize("email, pwd", TD_LOGIN)
    def test_favourite_recipe_registered(self, email, pwd):
        self.menu.main_menu().click()
        self.menu.menu_item_profile().click()
        time.sleep(2)
        self.login.input_email().send_keys(email)
        self.login.input_password().send_keys(pwd)
        self.login.button_login().click()
        time.sleep(2)
        assert "user-profile" in self.browser.current_url

        self.menu.main_menu().click()
        self.menu.menu_item_recipes().click()
        self.fav.click_recipe().click()
        self.fav.favourite_btn().click()
        time.sleep(2)
        assert self.fav.favourite_ok_btn().is_displayed()

        time.sleep(2)
        self.fav.favourite_ok_btn().click()
        assert self.fav.favourite_btn().is_displayed()

        self.menu.main_menu().click()
        self.menu.menu_item_profile().click()
        time.sleep(2)
        self.login.button_logout().click()
        time.sleep(2)
        assert "landing-page" in self.browser.current_url
