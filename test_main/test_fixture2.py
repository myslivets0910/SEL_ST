import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture # Декоратор, который определяет фикстуру. Фикстуры используются для настройки тестов.
def browser(): # фикстура, которая применяется в "def test_guest_should_see_login_link(self, browser):" - ниже по коду
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    # python -m pytest test_fixture1.py -s -v --tb=line     --- запуск теста
    # https://stepik.org/lesson/237257/step/3?unit=209645