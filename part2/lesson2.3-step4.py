from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
browser.find_element_by_css_selector('button[type=submit]').click()

confirm = browser.switch_to.alert
confirm.accept()

x = int(browser.find_element_by_css_selector('#input_value').text)
browser.find_element_by_css_selector('#answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type=submit').click()

time.sleep(5)