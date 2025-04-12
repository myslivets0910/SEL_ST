# моя ошибка была в том что я не редактировал код, а не писал программу.
# нужно было прописывать выводы и присвоение новых переменных

import math, time
import select

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    # открываем браузер и переходим на сайт
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    txt1 = browser.find_element(By.XPATH, '//*[@id="num1"]')
    # указали какой элемет ищем
    a = int(txt1.text) # приобразовали строковое значение в числовое
    # присвоили искомаму элементу переменную а
    print(a) # вывели переменную на печать (проверили что это тот элемент)

    txt2 = browser.find_element(By.XPATH, '//*[@id="num2"]')
    # указали какой элемет ищем
    b = int(txt2.text) # приобразовали строковое значение в числовое
    # присвоили искомаму элементу переменную b
    print(b) # вывели переменную на печать (проверили что это тот элемент)

    y = (a + b) # нашли сумму a и b
    print(str(y)) # вывели сумму

    drop1 = browser.find_element(By.XPATH, '//*[@id="dropdown"]')
    drop1.click()
    # раскрыли выпадающий список

    browser.find_element(By.CSS_SELECTOR, (f"[value='{y}']")).click()
    # нашли из выпадающего списка значение y и кликнули на него

    button = browser.find_element(By.CSS_SELECTOR, "button")
    # также поиск по By.TAG_NAME - Теги – это div, p, span, a, input, button и т.д.
    # также поиск по By.XPATH
    # находим кнопку с помощью селектора
    button.click()
    # нажимаем на кнопку

    # находим элемент куда вставляем значение y
    # y = calc(a + b) # производим расчет у (запускаем функцию для x)
    # print(y) # выводим результат функции на печать
    # input_1.send_keys(y) # вставляем результат функции в элемент в который нужно его вставить



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
