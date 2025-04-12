"""
  Программа проверяет, можно ли отправить форму без необязательных полей
  https://stepik.org/lesson/138920/step/10?unit=196194

  Тест падает для новой версии регистрации по ссылке:
  https://suninjuly.github.io/registration2.html
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def main():
    try:
        link = 'https://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_block = browser.find_element(By.CSS_SELECTOR, '.first_block')
        first_name = first_block.find_element(By.CSS_SELECTOR, '.form-control.first')
        last_name = first_block.find_element(By.CSS_SELECTOR, '.form-control.second')
        email = first_block.find_element(By.CSS_SELECTOR, '.form-control.third')

        first_name.send_keys('Greg')
        last_name.send_keys('House')
        email.send_keys('greg.house@md.com')

        button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
        button.click()
        
        sleep(5)
        welcome_text_elem = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elem.text

        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        sleep(15)
        browser.quit()

if __name__ == '__main__':
    main()