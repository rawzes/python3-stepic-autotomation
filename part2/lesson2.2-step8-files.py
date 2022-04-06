import os 
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/file_input.html')
browser.find_element_by_css_selector('input[name="firstname"]').send_keys('first')
browser.find_element_by_css_selector('input[name="lastname"]').send_keys('last')
browser.find_element_by_css_selector('input[name="email"]').send_keys('email@test.com')

file_name = 'file.txt'
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, file_name)   
browser.find_element_by_css_selector('#file').send_keys(file_path)

browser.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(10)
browser.quit()
