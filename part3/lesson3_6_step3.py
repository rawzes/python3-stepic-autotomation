import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url_list = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("urls", url_list)
class TestAliens:

    def test_answers_from_pages(self, browser, urls):
        browser.get(urls)
        area = browser.find_element_by_css_selector("textarea[required]")
        answer = math.log(int(time.time()))
        area.send_keys(str(answer))
        browser.find_element_by_css_selector("button.submit-submission").click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        )

        result = browser.find_element_by_css_selector("pre.smart-hints__hint")
        print(f"Actual text: {result.text}")
        assert "Correct!" == result.text, 'Text if not equal!'
