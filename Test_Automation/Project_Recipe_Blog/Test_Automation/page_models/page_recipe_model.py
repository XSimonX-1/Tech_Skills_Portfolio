from page_models.general_model import GeneralPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

URL = "http://localhost:4200"


class RecipesOfTheDay(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def rotd_section_item(self):
        return self.browser.find_element(By.CSS_SELECTOR, "img[class^='recipe-of-day']")


class SaveToPDF(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def recipe_item(self):
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='recipe-container ng-star-inserted']")))

    def save_as_pdf_btn(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='mt-4']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", button)
        return button


class WathCook(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def input_ingredient(self):
        return self.browser.find_element(By.ID, "ingredients")

    def button_add(self):
        return self.browser.find_element(By.XPATH, "//button[@class='btn__add-ingredient']")

    def button_what(self):
        return self.browser.find_element(By.XPATH, "//button[@class='mt-5 d-block m-auto']")

    def find_recipes(self):
        time.sleep(0.2)
        return self.browser.find_elements(By.XPATH,
            "//app-what-to-cook/div[@class='form-container']/div[@class='recipe-container ng-star-inserted']")


class FilterSection(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def input_category(self):
        return self.browser.find_element(By.ID, "categoryId")

    def button_difficulty_easy(self):
        # return self.browser.find_element(By.XPATH, "//input[@id='easy']/following-sibling::label")
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='easy']/following-sibling::label")))

    def button_difficulty_medium(self):
        return self.browser.find_element(By.XPATH, "//input[@id='medium']/following-sibling::label")

    def button_difficulty_hard(self):
        return self.browser.find_element(By.XPATH, "//input[@id='hard']/following-sibling::label")

    def button_price_cheap(self):
        return self.browser.find_element(By.XPATH, "//input[@id='1']/following-sibling::label")

    def button_price_medium(self):
        return self.browser.find_element(By.XPATH, "//input[@id='1,2']/following-sibling::label")

    def button_price_expensive(self):
        return self.browser.find_element(By.XPATH, "//input[@id='1,2,3']/following-sibling::label")

    def input_preparation_time(self):
        return self.browser.find_element(By.ID, "preparationTime")

    def output_preparation_time(self):
        return self.browser.find_element(By.ID, "num")

    def button_search(self):
        return self.browser.find_element(By.XPATH, "//button[@class='form-bottom-button' and text() = ' Search ']")

    def button_clear(self):
        return self.browser.find_element(By.XPATH, "//button[@class='form-bottom-button' and text() = ' Clear ']")

    def set_difficulty(self, difficulties=[]):
        for diff in difficulties:
            if diff.lower() == "easy":
                self.button_difficulty_easy().click()
            if diff.lower() == "medium":
                self.button_difficulty_medium().click()
            if diff.lower() == "hard":
                self.button_difficulty_hard().click()

    def set_price(self, prices=[]):
        for price in prices:
            if price.lower() == "cheap":
                self.button_price_cheap().click()
            if price.lower() == "medium":
                self.button_price_medium().click()
            if price.lower() == "expensive":
                self.button_price_expensive().click()

    def set_preparation_time(self, value=0):
        inp_prep_time = self.input_preparation_time()
        outp_prep_time = self.output_preparation_time()
        min_val = int(inp_prep_time.get_attribute("min")) or 0
        max_val = int(inp_prep_time.get_attribute("max")) or 100
        width = inp_prep_time.size["width"]
        diff = max_val - min_val
        unit = width / diff
        target = min(max_val, int((value - ((max_val - min_val) / 2)) * unit))

        ac = ActionChains(self.browser)

        ac.move_to_element_with_offset(inp_prep_time, -int(width / 2), 1)
        ac.click_and_hold()
        ac.move_by_offset(int(width), 0)

        ac.move_to_element_with_offset(inp_prep_time, target, 1)

        ac.release()
        ac.perform()

        while True:
            time_prep = outp_prep_time.text.replace('min', '').replace('more than', '')
            if time_prep == "":
                time_prep = "0"
            cur_val = int(time_prep)
            if cur_val == value or min_val > value or max_val < value:
                break

            if cur_val < value:
                step = unit
            else:
                step = -unit

            ac.click_and_hold(None)
            ac.move_by_offset(step, 0)
            ac.release(None)
            ac.perform()


class RecipesDisplay(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def choose_category(self):
        return self.browser.find_element(By.XPATH, "//div[@class='form-group mb-b mt-1 category-select-container']")

    def select_display(self):
        return Select(self.browser.find_element(By.ID, "select1"))

    def recipe_container(self):
        return self.browser.find_element(By.XPATH, "//div[@class='recipe-list-container']")

    def displayed_recipes(self):
        time.sleep(0.2)
        return self.browser.find_elements(By.CSS_SELECTOR, "div[class^='recipe-container']")

    def displayed_recipes_img(self):
        time.sleep(0.2)
        return self.browser.find_elements(By.XPATH, "//div[@class='recipe-container']//child::img")

    def pagination_elements(self):
        # return self.browser.find_elements(By.XPATH, "//li[@class='page-item ng-star-inserted']")
        return self.browser.find_elements(By.CSS_SELECTOR, "li[class^='page-item']:not([id^='chevron'])")

    def next_page(self):
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='fa-solid fa-chevron-right']")))

    def prev_page(self):
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='fa-solid fa-chevron-left']")))

    def dis_property_category(self):
        return self.browser.find_elements(By.XPATH, "//div[@class='recipe-header']/child::ul/child::li")

    def dis_property_times(self):
        return self.browser.find_elements(By.XPATH, "//li[@class='property property-time']/child::div")

    def dis_property_difficulties(self):
        return self.browser.find_elements(By.XPATH, "//li[@class='property property__difficulty']/child::div")

    def dis_property_costs(self):
        return self.browser.find_elements(By.XPATH, "//li[@class='property property__cost']/child::div")

    def page_body(self):
        return self.browser.find_element(By.CSS_SELECTOR, "body")

    def footer_links(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "footer-links")))

    def vote_values(self):
        return self.browser.find_elements(By.CLASS_NAME, "rating-values")

    def recipe_title(self):
        return self.browser.find_elements(By.CLASS_NAME, "recipe-title")

    def list_author_name(self):
        return self.browser.find_elements(By.XPATH, "//div[@class='author-name']")

    def get_page_first_recipe_title(self):
        title = None
        try:
            item = self.browser.find_element(By.CLASS_NAME, "recipe-title")
            title = item.text
        except StaleElementReferenceException:
            title = None
        return title

    def bottom_jump(self):
        time.sleep(0.5)
        bottom = self.page_body()
        bottom.send_keys(Keys.CONTROL + Keys.END)
        time.sleep(0.2)

    def get_displayed_recipes(self) -> int:
        # az oldal aljára navigálás
        time.sleep(0.2)
        self.bottom_jump()
        # az oldalakon végiglépkedve a megjelenített receptek összeszámolása
        pag_elements = self.pagination_elements()
        pages = len(pag_elements)
        if pages > 0:
            pag_elements[0].click()
        count = 0
        for i in range(pages):
            pag_elements[i].click()
            time.sleep(0.2)
            recipe_count = len(self.displayed_recipes())
            count += recipe_count

        return count

    def all_displayed_recipe_category_ok(self, category="") -> bool:
        ret = True
        if category != "":
            time.sleep(0.2)
            self.bottom_jump()
            pag_elements = self.pagination_elements()
            pages = len(pag_elements)
            if pages > 0:
                pag_elements[0].click()
            for i in range(pages):
                pag_elements[i].click()
                time.sleep(0.2)
                prop_category = self.dis_property_category()
                if len(prop_category) == 0:
                    ret = False
                for j in prop_category:
                    if j.text.replace('Category: ', '').lower() != category.lower():
                        ret = False
                        break
                if not ret:
                    break

            self.page_body().send_keys(Keys.PAGE_UP)

        return ret

    def all_displayed_recipe_difficulty_ok(self, difficulties=[str]) -> bool:
        ret = True
        if len(difficulties) != 0:
            # az oldal aljára navigálás
            time.sleep(0.2)
            self.bottom_jump()
            pag_elements = self.pagination_elements()
            pages = len(pag_elements)
            if pages > 0:
                pag_elements[0].click()
            s_diff = []
            for z in difficulties:
                s_diff.append(z.lower())
            for i in range(pages):
                pag_elements[i].click()
                time.sleep(0.2)
                prop_diff = self.dis_property_difficulties()
                if len(prop_diff) == 0:
                    ret = False
                for j in prop_diff:
                    if j.text not in set(s_diff):
                        ret = False
                        break
                if not ret:
                    break

            self.page_body().send_keys(Keys.PAGE_UP)

        return ret

    def all_displayed_recipe_price_ok(self, prices=[str]) -> bool:
        ret = True
        if len(prices) != 0:
            time.sleep(0.2)
            self.bottom_jump()
            pag_elements = self.pagination_elements()
            pages = len(pag_elements)
            if pages > 0:
                pag_elements[0].click()
            s_pric = []
            for z in prices:
                s_pric.append(z.lower())
            for i in range(pages):
                pag_elements[i].click()
                time.sleep(0.2)
                prop_cost = self.dis_property_costs()
                if len(prop_cost) == 0:
                    ret = False
                for j in prop_cost:
                    if j.text not in set(s_pric):
                        ret = False
                        break
                if not ret:
                    break

            self.page_body().send_keys(Keys.PAGE_UP)

        return ret

    def all_displayed_recipe_time_ok(self, max_time=0) -> bool:
        ret = True
        if max_time > 0:
            time.sleep(0.2)
            self.bottom_jump()
            pag_elements = self.pagination_elements()
            pages = len(pag_elements)
            if pages > 0:
                pag_elements[0].click()
            for i in range(pages):
                pag_elements[i].click()
                time.sleep(0.2)
                prop_time = self.dis_property_times()
                if len(prop_time) == 0:
                    ret = False
                for j in prop_time:
                    if int(j.text.replace("min", "")) > max_time:
                        ret = False
                        break
                if not ret:
                    break

            self.page_body().send_keys(Keys.PAGE_UP)

        return ret

    def get_followed_author_next_recipe(self, author_name: str, page_from: int, recipe_from: int):
        ret = {
            "page": -1,
            "recipe_pos": -1
        }

        time.sleep(0.2)
        self.bottom_jump()

        pag_elements = self.pagination_elements()
        pages = len(pag_elements)
        break_loop = False
        for i in range(page_from, pages):
            pag_elements[i].click()
            time.sleep(0.2)
            for j, item in enumerate(self.list_author_name()):
                if i == page_from and j <= recipe_from:
                    continue
                time.sleep(0.1)
                if item.text.find(author_name) != -1:
                    ret["page"] = i
                    ret["recipe_pos"] = j
                    break_loop = True
                    break
            if break_loop:
                break
        return ret

    def all_followed_auther_ok(self, author_name) -> bool:
        ret = True
        time.sleep(0.2)
        self.bottom_jump()

        pag_elements = self.pagination_elements()
        pages = len(pag_elements)
        break_loop = False
        for i in range(pages):
            pag_elements[i].click()
            time.sleep(0.2)
            for j, item in enumerate(self.list_author_name()):
                time.sleep(0.1)
                if item.text.find(author_name) != -1:
                    item.click()
                    break_loop = True
                    break
            if break_loop:
                break

        return ret

    def find_recipe_title(self, title: str) -> bool:
        ret = False
        self.bottom_jump()
        pag_elements = self.pagination_elements()
        pages = len(pag_elements)
        for i in range(pages):
            pag_elements[i].click()
            time.sleep(0.2)
            for j, item in enumerate(self.recipe_title()):
                if item.text == title:
                    item.click()
                    ret = True
                    break
            if ret:
                break

        return ret


class OneRecipePage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def page_body(self):
        return self.browser.find_element(By.CSS_SELECTOR, "body")

    def rating_container(self):
        return self.browser.find_element(By.CLASS_NAME, "ratings-container")

    def rating_stars(self):
        return self.browser.find_element(By.CLASS_NAME, "rating-stars")

    def rating_values(self):
        return self.browser.find_element(By.CLASS_NAME, "rating-values")

    def my_rating_stars(self):
        return self.browser.find_elements(By.XPATH, "//div[@class='my-rating ng-star-inserted']/child::i")

    def my_vote(self):
        return self.browser.find_elements(By.CSS_SELECTOR, "div[class^='my-rating']>i[class$='gold']")

    def input_author(self):
        return self.browser.find_element(By.XPATH, "//input[@formcontrolname='author']")

    def input_text(self):
        return self.browser.find_element(By.XPATH, "//textarea[@formcontrolname='commentBody']")

    def button_submit(self):
        return self.browser.find_element(By.XPATH, "//button[@type='submit']")

    def comment_info(self):
        return self.browser.find_elements(By.XPATH, "//h6[@class='text-info']")

    def comment_text(self):
        return self.browser.find_elements(By.XPATH, "//p[@class='text-muted']")

    def label_author(self):
        return self.browser.find_element(By.XPATH, "//div[@class='author-name']")

    def button_followed_author(self):
        try:
            btn = self.browser.find_element(By.XPATH, "//button[@class='btn-follow__bottom ng-star-inserted']")
        except NoSuchElementException or StaleElementReferenceException:
            btn = None
        return btn

    def favourite_btn(self):
        fav = WebDriverWait(self.browser, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-addToFavorites']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", fav)
        return fav

    def favourite_ok_btn(self):
        fav_ok = WebDriverWait(self.browser, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-addToFavorites addedToFavorites']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", fav_ok)
        return fav_ok

    def click_recipe(self):
        recipe_item = WebDriverWait(self.browser, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//img[@alt='image of dish']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", recipe_item)
        return recipe_item

    def set_vote(self, vote: int):
        ret = True
        my_rating_stars = self.my_rating_stars()
        my_vote = self.my_vote()
        if len(my_vote) - 1 != vote:
            rating_values_before = self.rating_values().text
            my_rating_stars[vote].click()
            i = 0
            while True:
                time.sleep(0.05)
                rating_values_after = self.rating_values().text
                if rating_values_before != rating_values_after or i == 100:
                    break
                i += 1
        return ret
