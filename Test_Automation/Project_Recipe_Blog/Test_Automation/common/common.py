import time
from selenium.webdriver.common.keys import Keys

def assert_handler(browser, exp: bool, message: str):
    if not exp:
        browser.save_screen('.', message)

    assert exp, message

def page_bottom_jump(act_page):
    time.sleep(0.5)
    bottom = act_page.page_body()
    bottom.send_keys(Keys.CONTROL + Keys.END)
    time.sleep(0.2)

