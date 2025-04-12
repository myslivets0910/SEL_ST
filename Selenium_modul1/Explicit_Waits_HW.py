import math, time
import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    # прописали функция на выполнение


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока значение на примет нужную цифру
    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "<От кого ждем>"), "<Что ждем>"))
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    # если появилось нужное значение, жмем на кнопку

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()


    # скролим в поле зрения элемента "название элемента"
    # browser.execute_script("return arguments[0].scrollIntoView(true);", элемент)

    txt1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    # указали какой элемет ищем
    x = txt1.text
    # присвоили искомаму элементу переменную х
    print(x) # вывели переменную на печать (проверили что это тот элемент)

    input_1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    # находим элемент куда вставляем значение y
    y = calc(x) # производим расчет у (запускаем функцию для x)
    print(y) # выводим результат функции на печать
    input_1.send_keys(y) # вставляем результат функции в элемент в который нужно его вставить

    submit1 = browser.find_element(By.XPATH, '//*[@id="solve"]')
    # ищем кнопку
    submit1.click()  # кликаем на кнопку


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()

