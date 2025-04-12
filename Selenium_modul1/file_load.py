# моя ошибка была в том что я не редактировал код, а не писал программу.
# нужно было прописывать выводы и присвоение новых переменных

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # открываем браузер и переходим на сайт
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)



    # запонить поле 1
    first_block = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]') # найти первое поле
    first_block.send_keys("один")
    # заполнить поле 2
    first_name = first_block.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
    first_name.send_keys("два")
    # заполнить поле 3
    last_name = first_block.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
    last_name.send_keys("три")



    # загрузить файл


    file_input = browser.find_element(By.XPATH,"//*[@id='file']")
    # нашли элемент "загрузить файл"
    file_input.send_keys("C:\\Users\\kabac\\environments\\selenium_course\\file.txt")
    # подгрузили файл по полному пути из директории (copy Path/Reference)


    # нажать кнопку - готово, только поменять
    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
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
