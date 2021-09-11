from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/execute_script.html'
browser.get(link)
x_element = browser.find_element_by_css_selector('#input_value')
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element) 

x = int(x_element.text)
browser.find_element_by_css_selector('#answer').send_keys(calc(x))
browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_css_selector('button[type=submit]').click()

time.sleep(5)
