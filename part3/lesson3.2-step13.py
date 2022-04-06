import unittest
from selenium import webdriver
import time


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        login = browser.find_element_by_css_selector('div.first_block .first')
        login.send_keys('First name')

        last_name = browser.find_element_by_css_selector('div.first_block .second')
        last_name.send_keys('Last name')

        email = browser.find_element_by_css_selector('div.first_block .third')
        email.send_keys('test@gmail.com')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Text if not equal!')
        browser.quit()

    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        login = browser.find_element_by_css_selector('div.first_block .first')
        login.send_keys('First name')

        last_name = browser.find_element_by_css_selector('div.first_block .second')
        last_name.send_keys('Last name')

        email = browser.find_element_by_css_selector('div.first_block .third')
        email.send_keys('test@gmail.com')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Text if not equal!')
        browser.quit()


if __name__ == '__main__':
    unittest.main()
