from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//button[text()='Заказать']"
    )

    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"
    )

    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoScooter')]"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoYandex')]"
    )


    FAQ_QUESTION_1 = (
        By.ID,
        "accordion__heading-0"
    )

    FAQ_QUESTION_2 = (
        By.ID,
        "accordion__heading-1"
    )

    FAQ_QUESTION_3 = (
        By.ID,
        "accordion__heading-2"
    )

    FAQ_QUESTION_4 = (
        By.ID,
        "accordion__heading-3"
    )

    FAQ_QUESTION_5 = (
        By.ID,
        "accordion__heading-4"
    )

    FAQ_QUESTION_6 = (
        By.ID,
        "accordion__heading-5"
    )

    FAQ_QUESTION_7 = (
        By.ID,
        "accordion__heading-6"
    )

    FAQ_QUESTION_8 = (
        By.ID,
        "accordion__heading-7"
    )

    FAQ_ANSWER_1 = (
        By.ID,
        "accordion__panel-0"
    )

    FAQ_ANSWER_2 = (
        By.ID,
        "accordion__panel-1"
    )

    FAQ_ANSWER_3 = (
        By.ID,
        "accordion__panel-2"
    )

    FAQ_ANSWER_4 = (
        By.ID,
        "accordion__panel-3"
    )

    FAQ_ANSWER_5 = (
        By.ID,
        "accordion__panel-4"
    )

    FAQ_ANSWER_6 = (
        By.ID,
        "accordion__panel-5"
    )

    FAQ_ANSWER_7 = (
        By.ID,
        "accordion__panel-6"
    )

    FAQ_ANSWER_8 = (
        By.ID,
        "accordion__panel-7"
    )



    def click_order_button_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(self.ORDER_BUTTON_BOTTOM)


    def click_order_button(self, position):
        if position == "top":
            self.click_order_button_top()
        elif position == "bottom":
            self.click_order_button_bottom()


    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    def open_main_page(self):
        self.open(self.URL)

    def click_faq_question(self, locator):
        self.click(locator)

    def get_faq_answer(self, locator):
        return self.get_text(locator)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

        