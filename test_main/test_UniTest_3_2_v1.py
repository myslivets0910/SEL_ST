import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def setUp(self): # setUp - метод, который выполняется перед каждым тестом и запускает браузер
        self.link1 = "  http://suninjuly.github.io/registration1.html"
        self.link2 = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()

    def fill_form_and_submit(self, link): # fill_form_and_submit - общий метод для заполнения форм и нажатия кнопок,
        # получение текста успешной регистрации, принимающий  URL страницы в качесте параметра
        self.browser.get(link)

        # Заполнение обязательных полей
        input1 = self.browser.find_element(By.XPATH, "//html/body/div[1]/form/div[1]/div[1]/input")
        input1.send_keys("Один")

        input2 = self.browser.find_element(By.XPATH, "//html/body/div[1]/form/div[1]/div[2]/input")
        input2.send_keys("Smolensk")

        input3 = self.browser.find_element(By.XPATH, "//html/body/div[1]/form/div[1]/div[3]/input")
        input3.send_keys("Три")

        input4 = self.browser.find_element(By.XPATH, "//html/body/div[1]/form/div[2]/div[1]/input")
        input4.send_keys("Четыре")

        input5 = self.browser.find_element(By.XPATH, "//html/body/div[1]/form/div[2]/div[2]/input")
        input5.send_keys("4")

        # Отправка формы
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ожидание загрузки страницы
        time.sleep(3)

        # Находим элемент приветствия
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        return welcome_text

    def test_registration1(self): # test_registration1/2 - методы тестируют регистрацию на соответствующих страница, использую общий метод fill_form_and_submit
        welcome_text = self.fill_form_and_submit(self.link1) # происходит вызов метода fill_form_and_submit с аргументом self.link1
        # где аргумент "self.link1" - обращается к атрибуту link1 этого экземпляра
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        # вызывается метод assertEqual, который используется для проверки равенства двух значений:
        # welcome_text и строки "Congratulations! You have successfully registered!".

    def test_registration2(self):
        welcome_text = self.fill_form_and_submit(self.link2)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        # вызывается метод assertEqual, который используется для проверки равенства двух значений:
        # welcome_text и строки "Congratulations! You have successfully registered!".

    def tearDown(self): # tearDown - метод выполняется после выполнения каждого теста и закрывает браузер, чтобы избежать утечек памяти
        # Ожидание для визуальной оценки результатов
        time.sleep(10)
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()