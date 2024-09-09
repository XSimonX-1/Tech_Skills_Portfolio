from config.configuration import get_preconfigured_chrome_driver
from page_models.page_navigator_model import MenuMain
from page_models.page_user_model import ContactPage
from page_models.page_user_model import LoginPage


class TestMainPage:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.main_menu = MenuMain(browser=self.browser)
        self.contact = ContactPage(browser=self.browser)
        self.login = LoginPage(browser=self.browser)
        self.main_menu.open()
        #self.main_menu.browser.maximize_window()
        self.main_menu.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    def test_contact_menu(self):
        self.main_menu.menu_item_click("contact")
        assert 'contact-page' in self.main_menu.current_url()
        contact_images = self.contact.list_images()
        assert len(contact_images) == 4

    def test_profile_menu(self):
        self.main_menu.menu_item_click("profile")
        assert self.browser.current_url.find('authentication') != -1

    def test_recipes_menu(self):
        self.main_menu.menu_item_click("recipes")
        assert self.browser.current_url.find('filter-form') != -1

    def test_home_menu(self):
        self.main_menu.menu_item_click("home")
        assert self.browser.current_url.find('landing-page') != -1
