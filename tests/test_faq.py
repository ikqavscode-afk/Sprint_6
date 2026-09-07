import allure
import pytest

from pages.main_page import MainPage


FAQ_DATA = [
    (
        "Проверка первого вопроса FAQ",
        MainPage.FAQ_QUESTION_1,
        MainPage.FAQ_ANSWER_1,
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ),
    (
        "Проверка второго вопроса FAQ",
        MainPage.FAQ_QUESTION_2,
        MainPage.FAQ_ANSWER_2,
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ),
    (
        "Проверка третьего вопроса FAQ",
        MainPage.FAQ_QUESTION_3,
        MainPage.FAQ_ANSWER_3,
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ),
    (
        "Проверка четвертого вопроса FAQ",
        MainPage.FAQ_QUESTION_4,
        MainPage.FAQ_ANSWER_4,
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ),
    (
        "Проверка пятого вопроса FAQ",
        MainPage.FAQ_QUESTION_5,
        MainPage.FAQ_ANSWER_5,
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ),
    (
        "Проверка шестого вопроса FAQ",
        MainPage.FAQ_QUESTION_6,
        MainPage.FAQ_ANSWER_6,
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ),
    (
        "Проверка седьмого вопроса FAQ",
        MainPage.FAQ_QUESTION_7,
        MainPage.FAQ_ANSWER_7,
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ),
    (
        "Проверка восьмого вопроса FAQ",
        MainPage.FAQ_QUESTION_8,
        MainPage.FAQ_ANSWER_8,
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    )
]


@pytest.mark.parametrize(
    "title, question_locator, answer_locator, expected_answer",
    FAQ_DATA
)
def test_faq_questions(
        driver,
        title,
        question_locator,
        answer_locator,
        expected_answer
):
    allure.dynamic.title(title)

    page = MainPage(driver)

    page.open_main_page()
    page.accept_cookies()

    page.click_faq_question(question_locator)

    actual_answer = page.get_faq_answer(answer_locator)

    assert actual_answer == expected_answer