import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_preconfigured_chrome_driver() -> webdriver.Chrome:
    options = Options()
    download_dir = os.getenv('RUNNER_TEMP', '/tests/Downloads')

    prefs = {'download.default_directory': '/Users/xxx/projektmunka-blog1/tests/Downloads'}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('detach', True)
    options.add_argument('--headless')
    #options.add_argument('window-position=-2000,-1000') #2 képernyő esetén
    #options.add_argument("--disable-search-engine-choice-screen")
    #options.add_argument("--lang=hu")
    # options.add_argument("--lang=en")
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Allure certificate error esetén

    return webdriver.Chrome(options=options)
