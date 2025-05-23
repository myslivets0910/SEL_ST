from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, '//*[@id="country"]')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[6]/button[3]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла