import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


'''
За допомогою assert можна перевіряти будь-яку конструкцію, яка повертає True/False. 
Це може бути перевірка рівності, нерівності, змісту підрядка у рядку або будь-яка інша допоміжна функція.

Якщо потрібно перевірити, що тест викликає очікуваний виняток (досить рідкісна ситуація для UI-тестів, 
і вам цей спосіб, швидше за все, ніколи не стане в нагоді), 
ми можемо використовувати спеціальну конструкцію with pytest.raises(). 
Наприклад, можна перевірити, що на сторінці сайту не повинен відображатись якийсь елемент
'''


def test_exception_1():
    try:
        browser = webdriver.Chrome()
        browser.get('https://casenik.com.ua/')
        # Оператор with використовується для обгортання виконання блоку за допомогою методів,
        # визначених менеджером контексту (див. розділ «Менеджери контексту операторів»)
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
