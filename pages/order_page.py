from datetime import datetime

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_customer_data(
            self,
            name,
            surname,
            address,
            phone
    ):
        self.find_element(
            OrderPageLocators.NAME_INPUT
        ).send_keys(name)

        self.find_element(
            OrderPageLocators.SURNAME_INPUT
        ).send_keys(surname)

        self.find_element(
            OrderPageLocators.ADDRESS_INPUT
        ).send_keys(address)

        self.find_element(
            OrderPageLocators.PHONE_INPUT
        ).send_keys(phone)

    def select_metro(self, metro):
        metro_input = self.find_element(
            OrderPageLocators.METRO_INPUT
        )

        metro_input.click()
        metro_input.send_keys(metro)

        metro_option = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(metro=metro)
        )

        self.click(metro_option)

    def fill_date(self, date):
        self.find_element(
            OrderPageLocators.DATE_INPUT
        ).send_keys(date)

    def select_date(self, date):
        self.find_element(
            OrderPageLocators.DATE_INPUT
        ).click()

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
            OrderPageLocators.DATE_OPTION[0],
            OrderPageLocators.DATE_OPTION[1].format(
                aria_label=aria_label
            )
        )

        self.click(date_element)

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    def get_success_message(self):
        return self.get_text(
            OrderPageLocators.SUCCESS_MESSAGE
        )

    def click_rental_period(self):
        self.click(OrderPageLocators.RENTAL_PERIOD)

    def select_rental_period(self, period):
        rental_option = (
            OrderPageLocators.RENTAL_OPTION[0],
            OrderPageLocators.RENTAL_OPTION[1].format(
                period=period
            )
        )

        self.click(rental_option)

    def select_color(self, color):
        color_locator = {
            "black": OrderPageLocators.BLACK_CHECKBOX,
            "grey": OrderPageLocators.GREY_CHECKBOX
        }

        self.click(color_locator[color])

    def fill_comment(self, comment):
        self.find_element(
            OrderPageLocators.COMMENT_INPUT
        ).send_keys(comment)

