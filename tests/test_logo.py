import allure

from pages.main_page import MainPage


@allure.title("Проверка возврата на главную страницу по логотипу Самокат")
def test_scooter_logo_returns_to_main_page(driver):
    page = MainPage(driver)

    page.open_main_page()
    page.accept_cookies()

    page.click_scooter_logo()

    assert page.get_current_url() == page.URL


@allure.title("Проверка перехода по логотипу Яндекс в Дзен") 
def test_yandex_logo_opens_dzen(driver): 
    page = MainPage(driver) 

    page.open_main_page() 
    page.accept_cookies() 

    old_window = driver.current_window_handle 

    page.click_yandex_logo() 

    page.switch_to_new_window(old_window) 
    page.wait.until( 
        lambda driver: "dzen.ru" in driver.current_url 
    ) 

    assert "dzen.ru" in driver.current_url