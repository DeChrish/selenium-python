# iframe.py
import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("frameid",[
    ("thedynamichtml"),
    ("theheaderhtml")
])

def test_iframe(browser : webdriver,frameid):
    expected = ['Colour','Date','Local date time','Email','Month','Number']
    browser.get("https://testpages.eviltester.com/styled/iframes-test.html")
    assert "iFrames Example" in browser.title

    browser.switch_to.frame(frameid)

    if "dynamic" in frameid:
        ids = browser.find_elements(By.TAG_NAME, "li")
    else:
        ids = browser.find_elements(By.TAG_NAME, "h1")
    print(len(ids))

    #iframe0  ul - li

    for id in ids:
        print(id.get_attribute('innerText'))