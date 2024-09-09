from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import WathCook
from page_models.page_navigator_model import PageHeader
from test_data_k import TD_SEARCH
import pytest
import sys
sys.path.append('/config/configuration.py')

class TestSearch:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.what_cook = WathCook(browser=self.browser)
        self.page_header = PageHeader(browser=self.browser)
        self.what_cook.open()
        #self.what_cook.browser.maximize_window()
        self.what_cook.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    @pytest.mark.parametrize("searched_text, expected_result", TD_SEARCH)
    def test_search(self, searched_text, expected_result):
        self.page_header.input_search().send_keys(searched_text)
        self.page_header.button_search().click()
        assert self.page_header.current_url().find(searched_text) > 0
        assert self.page_header.search_text().is_enabled()
        if expected_result:
            try:
                recipes_nr = len(self.page_header.recipes_list())
                print("Szám:", recipes_nr)
            except:
                recipes_nr = 0
            assert recipes_nr > 0
        else:
            try:
                nothing_text = self.page_header.nothing_found().text
            except:
                nothing_text = ""
            assert nothing_text == "Can't find what you're looking for?"