from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import FilterSection, RecipesDisplay
from page_models.page_navigator_model import MenuMain
from database.database_methods import get_recipes_number
from test_data_k import TD_FILTER
from common.common import assert_handler
import pytest


class TestFilter:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.section_filter = FilterSection(browser=self.browser)
        self.display_recipes = RecipesDisplay(browser=self.browser)
        self.main_menu = MenuMain(browser=self.browser)
        self.section_filter.open()
        #self.section_filter.browser.maximize_window()
        self.section_filter.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    @pytest.mark.parametrize("category, difficulties, prices, max_time", TD_FILTER)
    def test_filter(self, category, difficulties, prices, max_time):
        self.main_menu.menu_item_click("recipes")

        self.section_filter.input_category().send_keys(category)
        self.section_filter.set_difficulty(difficulties)
        self.section_filter.set_price(prices)
        self.section_filter.set_preparation_time(max_time)

        self.section_filter.button_search().click()

        total_count = get_recipes_number(category_name=category, difficulty_list=difficulties, cost_list=prices,
                                         max_prep_time=max_time)

        displayed_count = self.display_recipes.get_displayed_recipes()


        assert_handler(self.display_recipes, displayed_count == total_count, "test_filter_count")
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_category_ok(category),
                       "test_filter_category")
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_difficulty_ok(difficulties),
                       "test_filter_difficulty")
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_price_ok(prices),
                       "test_filter_price")
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_time_ok(max_time),
                       "test_filter_max_time")

    def test_category_filter(self):
        category = "soup"
        self.main_menu.menu_item_click("recipes")

        self.section_filter.input_category().send_keys(category)
        self.display_recipes.next_page().click()
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_category_ok(category),
                       "test_category_filter")

    def test_difficulty_filter(self):
        difficulties = ["hard"]
        self.main_menu.menu_item_click("recipes")

        self.section_filter.set_difficulty(difficulties)
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_difficulty_ok(difficulties),
                       "test_difficulty_filter")

    def test_price_filter(self):
        prices = ["medium"]
        self.main_menu.menu_item_click("recipes")

        self.section_filter.set_price(prices)
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_price_ok(prices),
                       "test_price_filter")

    def test_max_time_filter(self):
        max_time = 30
        self.main_menu.menu_item_click("recipes")

        self.section_filter.set_preparation_time(max_time)
        assert_handler(self.display_recipes, self.display_recipes.all_displayed_recipe_time_ok(max_time),
                       "test_max_time_filter")
