# elements_list.py
import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_table(browser : webdriver):

    expected = ['Colour','Date','Local date time','Email','Month','Number']
    browser.get("https://testpages.eviltester.com/styled/html5-form-test.html")
    assert "HTML5 Form Elements Test Page" in browser.title
    count = 0
    ids = browser.find_elements(By.CSS_SELECTOR, '#HTMLFormElements div label')
    print(len(ids))
    for id in ids:
        actual = id.get_attribute('innerText')
        actual_list = actual[:-2]
        assert actual_list in expected[count]
        count = count + 1
        