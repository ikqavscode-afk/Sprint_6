# Sprint_6

Автоматизированное тестирование учебного сервиса «Самокат».

## Что тестируется

В проекте реализованы UI-тесты с использованием Selenium:

* проверка вопросов и ответов в разделе «Вопросы о важном»;
* оформление заказа через верхнюю и нижнюю кнопки «Заказать»;
* проверка двух наборов данных для оформления заказа;
* проверка перехода по логотипу «Самокат»;
* проверка перехода по логотипу «Яндекс» в Дзен.

Всего реализовано 14 тестовых сценариев.

## Технологии

* Python
* pytest
* Selenium
* Allure
* Page Object Model

## Структура проекта

pages/
├── base_page.py
├── main_page.py
└── order_page.py

tests/
├── test_faq.py
├── test_logo.py
└── test_order.py

conftest.py
pytest.ini
requirements.txt

## Установка

Создать виртуальное окружение:

python3 -m venv .venv


Активировать его:

source .venv/bin/activate


Установить зависимости:

pip install -r requirements.txt


## Запуск тестов

Запустить все тесты:

pytest -v


Ожидаемый результат:

14 passed


## Allure

Сформировать результаты тестирования:

pytest --alluredir=allure-results


Открыть отчёт:

allure serve allure-results
