from selenium import webdriver
import time

url = 'http://suninjuly.github.io/find_xpath_form'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_name('first_name').send_keys('test1')
browser.find_element_by_name('last_name').send_keys('test2')
browser.find_element_by_name('firstname').send_keys('test3')
browser.find_element_by_id('country').send_keys('test4')

submit_button = browser.find_element_by_xpath("//button[text()='Submit']")
submit_button.click()

time.sleep(10)
browser.quit()