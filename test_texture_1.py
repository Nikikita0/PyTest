from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://casenik.com.ua/'


class TestPage1():

    @classmethod
    def setup_class(self):  # будет влиять на весь класс
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):  # будет влиять на весь класс
        print("\nquit browser for test suite..")
        self.browser.quit()

    def test_is_button_search(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//button[@class= 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//a[@href = 'cart/show']")

