from pages.base_page import BasePage
from constants import SCOOTER_URL
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def open_main_page(self):
        self.open(SCOOTER_URL)

    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_order_button(self, position):
        if position == "top":
            self.click_order_button_top()
        elif position == "bottom":
            self.click_order_button_bottom()

    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    def click_faq_question(self, locator):
        self.click(locator)

    def get_faq_answer(self, locator):
        return self.get_text(locator)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
        