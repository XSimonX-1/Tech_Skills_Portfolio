import pytest
from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import RecipesOfTheDay


@pytest.mark.flaky(rerun=2) #Rerun X times if fails
class TestRecipesOfTheDay:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.rotd_section = RecipesOfTheDay(browser=self.browser)
        self.rotd_section.open()
        #self.rotd_section.browser.maximize_window()
        self.rotd_section.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    def test_recipes_of_the_day(self):
        self.rotd_section.rotd_section_item().click()
        assert "recipes" in self.browser.current_url