import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


@pytest.mark.parametrize(
    "order_button",
    ["top", "bottom"]
)

@pytest.mark.parametrize(
    "name, surname, address, phone, metro, date, rental_period, color, comment",
    ORDER_DATA
)

def test_order_customer_data(
        driver,
        order_button,
        name,
        surname,
        address,
        phone,
        metro,
        date,
        rental_period,
        color,
        comment
):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.accept_cookies()

    main_page.click_order_button(order_button)

    order_page.fill_customer_data(
        name=name,
        surname=surname,
        address=address,
        phone=phone
    )

    order_page.select_metro(metro)

    order_page.click_next()

    order_page.select_date(date)

    order_page.click_rental_period()
    order_page.select_rental_period(rental_period)

    order_page.select_color(color)

    order_page.fill_comment(comment)

    order_page.click_order()

    order_page.confirm_order()

    assert "Заказ оформлен" in order_page.get_success_message()
