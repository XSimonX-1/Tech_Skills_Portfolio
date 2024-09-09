import time
from selenium.common import ElementClickInterceptedException
from page_models.general_model import GeneralPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://localhost:4200"


class LoginPage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def input_email(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, "email")))

    def input_password(self):
        return self.browser.find_element(By.ID, "password")

    def button_login(self):
        return self.browser.find_element(By.XPATH, "//button[@type='submit']")

    def button_sign_up(self):
        signup = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='btn-ghost']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", signup)
        for attempt in range(5):
            try:
                signup.click()
                return signup
            except ElementClickInterceptedException:
                time.sleep(1)
                self.browser.execute_script("arguments[0].scrollIntoView(true);", signup)
        raise Exception("Unable to click the sign-up button after multiple attempts.")

    def label_email(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "h6")))

    def button_logout(self):
        logout = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='logout']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", logout)
        return logout

    def button_followed_author(self):
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='My Followed Authors']")))

    def login_k(self, email, password):
        ret = False
        try:
            self.input_email().send_keys(email)
            self.input_password().send_keys(password)
            self.button_login().click()
            time.sleep(1)
            # self.label_email().text
            if "user-profile" in self.browser.current_url:
                ret = True
        except:
            pass
        return ret

    def login_s(self, email, password):
        try:
            self.input_email().send_keys(email)
            self.input_password().send_keys(password)
            self.button_login().click()
            #self.label_email().text
            ret = True
        except:
            ret = False
        return ret


class RegistrationPage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def input_email(self):
        return self.browser.find_element(By.ID, "email")

    def input_name(self):
        return self.browser.find_element(By.ID, "name")

    def input_pwd(self):
        return self.browser.find_element(By.ID, "password")

    def submit_btn(self):
        s_btn = WebDriverWait(self.browser, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", s_btn)
        return s_btn


class ProfilePage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def button_my_followed_author(self):
        choose_section = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "choose-section")))
        return choose_section.find_element(By.XPATH, "//p[text()='My Followed Authors']")

    def table_followed(self):
        return self.browser.find_element(By.XPATH, "//table[@class='table']/tbody")

    def followed_author_ok(self, author_email: str) -> bool:
        ret = False
        table = self.table_followed()
        for row in table.find_elements(By.TAG_NAME, "tr"):
            if ret:
                break
            for column in row.find_elements(By.XPATH, "td[@class='col-4']"):
                if column.text == author_email:
                    ret = True
                    break
        return ret

    def delete_followed_author(self, author_email: str):
        table = self.table_followed()
        flag_break = False
        for row in table.find_elements(By.TAG_NAME, "tr"):
            if flag_break:
                break
            for column in row.find_elements(By.XPATH, "td[@class='col-4']"):
                if column.text == author_email:
                    row.find_element(By.XPATH, "td/button").click()
                    flag_break = True
                    break


class ContactPage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url=URL)

    def list_images(self):
        return self.browser.find_elements(By.TAG_NAME, "img")
