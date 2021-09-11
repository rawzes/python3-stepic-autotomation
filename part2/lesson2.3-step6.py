from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')
#get current window
current_window = browser.current_window_handle
print('current window ', current_window)
#time.sleep(2)
element = browser.find_element_by_tag_name('button')
element.click()
print('list windows', browser.window_handles)
browser.switch_to_window(browser.window_handles[1])

x = int(browser.find_element_by_css_selector('#input_value').text)
browser.find_element_by_css_selector('#input_value')
browser.find_element_by_css_selector('#answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type=submit]').click()

time.sleep(5)
browser.quit()