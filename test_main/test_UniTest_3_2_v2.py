import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def link(linked):
    browser = webdriver.Chrome()
    browser.get(linked)

    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys('Smolensk')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    return welcome_text_elt.text
    browser.quit()


class TestLink(unittest.TestCase):

    def test_link1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(link(link1), "Congratulations! You have successfully registered!")

    def test_link2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(link(link2), "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    unittest.main()