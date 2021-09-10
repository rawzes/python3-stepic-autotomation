from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/selects1.html'
    link2 = 'http://suninjuly.github.io/selects2.html'
    browser.get(link)
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    result = num1 + num2

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(result))
    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()