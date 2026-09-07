from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from datetime import datetime



class OrderPage(BasePage):

    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )



    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    RENTAL_PERIOD = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']"
    )

    BLACK_CHECKBOX = (
        By.ID,
        "black"
    )

    GREY_CHECKBOX = (
        By.ID,
        "grey"
    )

    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    NEXT_BUTTON = (
    By.XPATH,
    "//button[text()='Далее']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"
    )

    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Да']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'Заказ оформлен')]"
    )

    STATUS_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Посмотреть статус']"
    )




    def fill_customer_data(
            self,
            name,
            surname,
            address,
            phone
    ):
        self.find_element(self.NAME_INPUT).send_keys(name)
        self.find_element(self.SURNAME_INPUT).send_keys(surname)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)
        self.find_element(self.PHONE_INPUT).send_keys(phone)

    def select_metro(self, metro):
        metro_input = self.find_element(self.METRO_INPUT)

        metro_input.click()
        metro_input.send_keys(metro)

        metro_option = (
            By.XPATH,
            f"//*[normalize-space(text())='{metro}']"
        )

        self.click(metro_option)


    def fill_date(self, date):
        self.find_element(self.DATE_INPUT).send_keys(date)

    def select_date(self, date):
        self.find_element(self.DATE_INPUT).click()

        date_obj = datetime.strptime(date, "%d.%m.%Y")

        months = {
            1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря"
        }

        weekdays = {
            0: "понедельник",
            1: "вторник",
            2: "среда",
            3: "четверг",
            4: "пятница",
            5: "суббота",
            6: "воскресенье"
        }

        aria_label = (
            f"Choose {weekdays[date_obj.weekday()]}, "
            f"{date_obj.day}-е {months[date_obj.month]} "
            f"{date_obj.year} г."
        )

        date_element = (
            By.XPATH,
            f"//div[@role='button' and @aria-label=\"{aria_label}\"]"
        )

        self.click(date_element)


    def click_next(self):
        self.click(self.NEXT_BUTTON)

    def click_order(self):
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def click_status(self):
        self.click(self.STATUS_BUTTON)
        

    def click_rental_period(self):
        self.click(self.RENTAL_PERIOD)

    def select_rental_period(self, period):
        rental_option = (
            By.XPATH,
            f"//div[@role='option' and text()='{period}']"
        )

        self.click(rental_option)


    def select_color(self, color):
        color_locator = {
            "black": self.BLACK_CHECKBOX,
            "grey": self.GREY_CHECKBOX
        }

        self.click(color_locator[color])

    def fill_comment(self, comment):
        self.find_element(self.COMMENT_INPUT).send_keys(comment)

