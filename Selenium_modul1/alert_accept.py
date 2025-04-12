# Переделать с CSS.celector



import math, time
import select

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    # прописали функция на выполнение

try:
    # открываем браузер и переходим на сайт
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # b_1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
    # b_1 = browser.find_element(By.CSS_SELECTOR,'button').click()
    # b_1 = browser.find_element(By.CLASS_NAME,'btn').click()
    b_1 = browser.find_element(By.TAG_NAME, 'button').click()
    # Нашли элемент на странице и кликнули на него

    alert = browser.switch_to.alert # определили модалку (alert = тревога)
    alert.accept() # совершили действие (accept = принимать) на модалке


    # txt1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    # txt1 = browser.find_element(By.ID,'input_value')
    txt1 = browser.find_element(By.CSS_SELECTOR,'#input_value')
    # указали какой элемет ищем
    x = txt1.text
    # присвоили искомаму элементу переменную х
    print(x) # вывели переменную на печать (проверили что это тот элемент)

    # input_1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    # input_1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_1 = browser.find_element(By.ID,'answer')

    # находим элемент куда вставляем значение y
    y = calc(x) # производим расчет у (запускаем функцию для x)
    print(y) # выводим результат функции на печать
    input_1.send_keys(y) # вставляем результат функции в элемент в который нужно его вставить

    # submit1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    # submit1 = browser.find_element(By.CLASS_NAME, 'btn-primary')
    # submit1 = browser.find_element(By.CLASS_NAME, 'btn').click()
    submit1 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()  # кликаем на кнопку
    # последний вариант селектор из панели диспетчера



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
