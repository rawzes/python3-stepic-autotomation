from selenium import webdriver
import time
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # элемент button, к которому нужно будет проскроллить страницу
button.click()

browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 100);") # similar variant
button.click()

'''
Как вариант еще можно скрывать ненужный элемент
browser.execute_script('arguments[0].style.visibility = \'hidden\'', foot

Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body
from selenium.webdriver.common.keys import Keys
browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх
'''

time.sleep(5)