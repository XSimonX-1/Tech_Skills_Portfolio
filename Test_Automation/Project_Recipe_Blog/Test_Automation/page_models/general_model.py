from datetime import datetime
from selenium.webdriver import Chrome


class GeneralPage:
    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.browser.set_window_size(1920, 1080)

    def close(self):
        self.browser.close()

    def refresh(self):
        self.refresh()

    def current_url(self):
        return self.browser.current_url

    def save_screen(self, path, name=''):
        filename = name
        if filename == '':
            filename = f'{self.browser.title}'
        filename += f'-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.jpg'
        print(rf'Screenshot attempt: {path}\{filename}')
        if self.browser.save_screenshot(f'{path}\\{filename}'):
            print("Screenshot saved successfully.")
        else:
            print("Screenshot failed.")
