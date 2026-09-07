import allure
import pytest

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data.faq_data import FAQ_DATA


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