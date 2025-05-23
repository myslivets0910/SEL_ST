import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function") #фикстура browser отрабатывает на уровне функций def, т.к. указан scope="function"
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser # финализатор который закрывает браузер
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke # маркировка тестов как smoke
    # Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression # маркировка тестов как regress
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")