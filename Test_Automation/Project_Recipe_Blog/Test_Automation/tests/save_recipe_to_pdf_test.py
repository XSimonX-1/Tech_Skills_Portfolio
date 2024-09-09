import time
import os
from config.configuration import get_preconfigured_chrome_driver
from page_models.page_recipe_model import SaveToPDF
from page_models.page_navigator_model import MenuMain


class TestSaveToPDF:
    download_dir = os.getenv('RUNNER_TEMP', '/Users/xxx/projektmunka-blog1/tests/Downloads')

    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.main_menu = MenuMain(browser=self.browser)
        self.save_pdf = SaveToPDF(browser=self.browser)
        self.main_menu.open()
        #self.main_menu.browser.maximize_window()
        self.main_menu.browser.set_window_size(1920, 1080)

    def teardown_method(self):
        self.browser.close()

    def latest_download_file(self, download_dir):
        files = os.listdir(download_dir)
        files = [f for f in files if os.path.isfile(os.path.join(download_dir, f))]
        files.sort(key=lambda f: os.path.getmtime(os.path.join(download_dir, f)))
        return files[-1] if files else None

    def test_save_to_pdf(self):
        self.main_menu.main_menu().click()
        self.main_menu.menu_item_recipes().click()
        self.save_pdf.recipe_item().click()
        assert "recipes" in self.browser.current_url
        time.sleep(2)

        save_btn = self.save_pdf.save_as_pdf_btn()
        time.sleep(3)
        save_btn.click()
        time.sleep(3)

        max_wait_time = 60
        start_time = time.time()
        newest_file = None
        while (time.time() - start_time) < max_wait_time:
            time.sleep(1)
            newest_file = self.latest_download_file(self.download_dir)
            if newest_file and not newest_file.endswith((".crdownload", ".sh")): #check temporary file
                break

        print("Contents of download directory:", os.listdir(self.download_dir))

        assert newest_file is not None, "No file was downloaded."
        assert newest_file.endswith('.pdf'), f"Expected a PDF file, but got {newest_file}"

        file_path = os.path.join(self.download_dir, newest_file)
        assert os.path.exists(file_path), f"File does not exist: {file_path}"