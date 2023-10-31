# iframe.py
from time import sleep
import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_iframe(browser : webdriver):
    expected = ['Colour','Date','Local date time','Email','Month','Number']
    browser.get("https://testpages.eviltester.com/styled/iframes-test.html")
    assert "iFrames Example" in browser.title

    #iframe = browser.find_element(By.ID, "#thedynamichtml")

    browser.switch_to.frame('thedynamichtml')

    ids = browser.find_elements(By.TAG_NAME, "li")

    print(len(ids))

    #iframe0  ul - li

    for id in ids:
        print(id.get_attribute('innerText'))