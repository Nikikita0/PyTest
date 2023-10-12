import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://casenik.com.ua/'

@pytest.fixture # для каждой функции

#@pytest.fixture(scope="class")  # для целого класса
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Авто использование текстур
@pytest.fixture(autouse=True)  # автоиспользование фикстур
def prepare():
    print('Печатай каждый тест')


class TestPage1():
    def test_is_button_search(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class= 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")
