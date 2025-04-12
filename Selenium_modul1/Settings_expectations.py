import math, time
import select

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # открываем браузер и переходим на сайт
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд

    # time.sleep(2)
    button = browser.find_element(By.XPATH, "//*[@id='verify']").click()
    #time.sleep(2)
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

