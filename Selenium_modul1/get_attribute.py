# моя ошибка была в том что я не редактировал код, а не писал программу.
# нужно было прописывать выводы и присвоение новых переменных

import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    # прописали функция на выполнение

try:
    # открываем браузер и переходим на сайт
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    txt1 = browser.find_element(By.XPATH, '//*[@id="treasure"]').get_attribute('valuex')
    # указали какой элемет ищем, для того чтобы вытащить из него атрибут
    x = txt1
    # прописываем атрибут для поиска в елементе

    # присвоили искомаму элементу переменную х
    print(x) # вывели переменную на печать (проверили что это тот элемент)

    input_1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    # находим элемент куда вставляем значение y
    y = calc(x) # производим расчет у (запускаем функцию для x)
    print(y) # выводим результат функции на печать
    input_1.send_keys(y) # вставляем результат функции в элемент в который нужно его вставить


    CH1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    # ищем чекбокс на странице
    CH1.click() # кликаем на чекбокс
    Rule2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    # ищем нужную радиокнопку
    Rule2.click() # кликаем на радиокнопку
    submit1 =browser.find_element(By.XPATH, '/html/body/div[1]/form/div/div/button')
    # ищем кнопку
    submit1.click() # кликаем на кнопку
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
