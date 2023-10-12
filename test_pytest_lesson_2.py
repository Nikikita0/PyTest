import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


'''

'''


def test_exception_1():
    try:
        browser = webdriver.Chrome()
        browser.get('https://casenik.com.ua/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300]")
            pytest.fail('Не повинно бути кнопки')
    finally:
        browser.quit()


def test_exception_2():
    try:
        browser = webdriver.Chrome()
        browser.get('https://casenik.com.ua/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button")
            pytest.fail('Не повинно бути кнопки')
    finally:
        browser.quit()
