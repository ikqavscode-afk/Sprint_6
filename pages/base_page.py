from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def switch_to_new_window(self, old_window):
        self.wait.until(
            lambda driver: len(driver.window_handles) > 1
        )

        new_window = [
            window
            for window in self.driver.window_handles
            if window != old_window
        ][0]

        self.driver.switch_to.window(new_window)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def wait_for_url_contains(self, text):
        self.wait.until(
            lambda driver: text in driver.current_url
        )