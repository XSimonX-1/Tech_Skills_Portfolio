from page_models.general_model import GeneralPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

URL = "http://localhost:4200"


class MenuMain(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def main_menu(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inner']")))

    def menu_item_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "contact")))

    def menu_item_profile(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "about-link")))

    def menu_item_recipes(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "recipe-list-link")))

    def menu_item_home(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "landing-page-link")))

    def menu_item_click(self, item_name):
        menu_main = self.main_menu()
        menu_main.click()
        time.sleep(0.1)
        if item_name == "contact":
            menu_item = self.menu_item_contact()
        elif item_name == "profile":
            menu_item = self.menu_item_profile()
        elif item_name == "recipes":
            menu_item = self.menu_item_recipes()
        elif item_name == "home":
            menu_item = self.menu_item_home()
        else:
            menu_item = None

        if menu_item is not None:
            menu_item.click()


class PageHeader(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def input_search(self):
        return self.browser.find_element(By.ID, "search-input")

    def button_search(self):
        return self.browser.find_element(By.XPATH, "//button[@class='btn-search']")

    def button_back(self):
        return self.browser.find_element(By.XPATH, "//button[@class='btn-back']")

    def search_text(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h4[@class='ng-star-inserted']")))

    def nothing_found(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='nothing-found ng-star-inserted']/h3")))

    def recipes_list(self):
        time.sleep(0.2)
        return self.browser.find_elements(By.XPATH, "//img[@class='img-fluid recipe-img']")


class PageFooter(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def link_dishub(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/']")))

    def link_facebook(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "facebook")))

    def link_instagram(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "instagram")))
