from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    expected_price = 100
    browser.get(url)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), str(expected_price))
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_value = browser.find_element_by_id('input_value').text
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(calc(x_value)))

    submit = browser.find_element_by_id('solve')
    submit.click()
    time.sleep(10)
finally:
    browser.quit()
