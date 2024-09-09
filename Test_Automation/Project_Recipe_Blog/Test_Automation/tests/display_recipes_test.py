from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import RecipesDisplay
from database.database_methods import get_recipes_number
from common.common import page_bottom_jump, assert_handler
from test_data_k import TD_RECIPE_NR
import pytest


class TestDisplayRecipes:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.display_recipes = RecipesDisplay(browser=self.browser)
        self.display_recipes.open()
        #self.display_recipes.browser.maximize_window()
        self.display_recipes.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    @pytest.mark.parametrize("recipe_per_page", TD_RECIPE_NR)
    def test_recipes_display(self, recipe_per_page):
        total_count = get_recipes_number()
        self.display_recipes.select_display().select_by_visible_text(str(recipe_per_page))

        assert len(self.display_recipes.displayed_recipes()) <= recipe_per_page

        count = self.display_recipes.get_displayed_recipes()
        assert count == total_count

    def test_pagination(self):
        page_bottom_jump(self.display_recipes)
        first_title = self.display_recipes.get_page_first_recipe_title()
        pages_nr = self.display_recipes.pagination_elements()
        page = int(len(pages_nr) / 2)
        pages_nr[page].click()
        while True:
            act_title = self.display_recipes.get_page_first_recipe_title()
            if act_title is not None and act_title != first_title:
                break

        self.display_recipes.displayed_recipes()[0].click()
        self.browser.back()
        page_bottom_jump(self.display_recipes)
        title_now = self.display_recipes.get_page_first_recipe_title()
        assert_handler(self.display_recipes, title_now == act_title, "test_pagination")
