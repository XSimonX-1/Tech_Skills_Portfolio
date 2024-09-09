from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import RecipesDisplay, OneRecipePage
from page_models.page_navigator_model import MenuMain
from page_models.page_user_model import LoginPage, ProfilePage
from common.common import page_bottom_jump, assert_handler
from test_data_k import TD_RATING, TD_COMMENT, TD_FOLLOW_AUTHOR
import time, datetime, pytest


class TestRecipe:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.recipe = OneRecipePage(browser=self.browser)
        self.main_menu = MenuMain(browser=self.browser)
        self.login = LoginPage(browser=self.browser)
        self.display_recipes = RecipesDisplay(browser=self.browser)
        self.profile = ProfilePage(browser=self.browser)
        self.recipe.open()
        #self.recipe.browser.maximize_window()
        self.recipe.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    @pytest.mark.parametrize("email, pwd, recipe_title", TD_RATING)
    def test_rating(self, email, pwd, recipe_title):
        self.main_menu.menu_item_click("profile")
        login_result = self.login.login_k(email, pwd)
        assert login_result, "Belépés sikertelen"

        self.main_menu.menu_item_click("recipes")
        recipe_find_result = self.display_recipes.find_recipe_title(recipe_title)
        assert recipe_find_result, "Receptet nem találtam."

        time.sleep(0.2)
        my_vote = self.recipe.my_vote()
        vote = len(my_vote) - 1
        if vote == 4:
            vote -= 1
        else:
            vote += 1
        rating_before = self.recipe.rating_values().text

        self.recipe.set_vote(vote)

        rating_after = self.recipe.rating_values().text
        assert rating_before != rating_after

    @pytest.mark.parametrize("email, pwd, recipe_title, nev, comment", TD_COMMENT)
    def test_comment(self, email, pwd, recipe_title, nev, comment):
        self.main_menu.menu_item_click("profile")
        login_result = self.login.login_k(email, pwd)
        assert login_result, "Belépés sikertelen"

        self.main_menu.menu_item_click("recipes")
        recipe_find_result = self.display_recipes.find_recipe_title(recipe_title)
        assert recipe_find_result, "Receptet nem találtam."
        page_bottom_jump(self.recipe)
        self.recipe.input_author().send_keys(nev)
        self.recipe.input_text().send_keys(comment)
        self.recipe.button_submit().click()
        time.sleep(0.5)
        x = datetime.datetime.now()
        pos = self.recipe.comment_info()[0].text.find(f"{nev} - {x.strftime('%Y-%m-%d ')}".strip())
        assert_handler(self.recipe, pos != -1, "test_comment")
        assert self.recipe.comment_text()[0].text == comment

    @pytest.mark.parametrize("email, pwd, author_name, author_email", TD_FOLLOW_AUTHOR)
    def test_follow_author(self, email, pwd, author_name, author_email):
        self.main_menu.menu_item_click("profile")
        login_result = self.login.login_k(email, pwd)
        assert login_result, "Belépés sikertelen"

        self.main_menu.menu_item_click("recipes")

        ret = self.display_recipes.get_followed_author_next_recipe(author_name=author_name, page_from=0, recipe_from=-1)
        print(ret)
        if ret["page"] != -1:
            self.display_recipes.pagination_elements()[ret["page"]].click()
            self.display_recipes.displayed_recipes()[ret["recipe_pos"]].click()

            btn_followed = self.recipe.button_followed_author()
            page_bottom_jump(self.recipe)
            if btn_followed is not None:
                btn_followed.click()
            time.sleep(0.5)
            btn_followed_again = self.recipe.button_followed_author()
            # 'FOLLOW AUTHOR' gomb eltűnik
            assert btn_followed_again is None

            self.main_menu.menu_item_click("profile")
            self.profile.button_my_followed_author().click()
            assert self.profile.followed_author_ok(author_email=author_email)


    @pytest.mark.parametrize("email, pwd, author_name, author_email", TD_FOLLOW_AUTHOR)
    def test_not_follow_author(self, email, pwd, author_name, author_email):
        self.main_menu.menu_item_click("profile")
        login_result = self.login.login_k(email, pwd)
        assert login_result, "Belépés sikertelen"

        self.main_menu.menu_item_click("profile")
        self.profile.button_my_followed_author().click()
        if self.profile.followed_author_ok(author_email=author_email):
            self.profile.delete_followed_author(author_email=author_email)
            time.sleep(0.5)
            assert not self.profile.followed_author_ok(author_email=author_email)
