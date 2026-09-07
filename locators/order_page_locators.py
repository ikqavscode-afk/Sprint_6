from selenium.webdriver.common.by import By


class OrderPageLocators:

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

    METRO_OPTION = (
        By.XPATH,
        "//*[normalize-space(text())='{metro}']"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    DATE_OPTION = (
        By.XPATH,
        "//div[@role='button' and @aria-label=\"{aria_label}\"]"
    )

    RENTAL_PERIOD = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']"
    )

    RENTAL_OPTION = (
        By.XPATH,
        "//div[@role='option' and text()='{period}']"
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
