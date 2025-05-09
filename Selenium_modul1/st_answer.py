from selenium import webdriver
import pytest
import time
import math

list_of_subpages = ['236895', '236896', '236897', #subpage numbers of Stepik lessons
                    '236898', '236899', '236903',
                    '236904', '236905']

def get_time_fun():
    return math.log(int(time.time())) # return temporarily valid answer for problems

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome() # run before every test_* function
    browser.implicitly_wait(10) # WebDriver wait response for 10s and try to find element every 500ms
    yield browser
    browser.quit() # teardown (run after evry test_* functions)

@pytest.mark.parametrize('page_num', list_of_subpages)
def test_solving_task(browser, page_num): # run for every Stepik lessons with substrings in list
    link = "https://stepik.org/lesson/{}/step/1".format(page_num)
    browser.get(link)
    anser_filed = browser.find_element_by_css_selector('.textarea') # find answer area
    anser_filed.send_keys(str(get_time_fun())) # write the answer
    submit_btn = browser.find_element_by_css_selector('.submit-submission') # find submit button
    submit_btn.click()
    hint_message = browser.find_element_by_css_selector('.smart-hints__hint') # find message of optional feedback
    assert hint_message.text == 'Correct!', 'Fail in test on page {}'.format(link) # compare with expexted answer