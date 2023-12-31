# test_login.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# def test_successful_login(browser: WebDriver):
#     browser.get("https://testpages.eviltester.com/styled/alerts/fake-alert-test.html")
#     assert "Fake Alerts" in browser.title
#     sleep(5)

def test_alert(browser: webdriver):
    browser.get("https://testpages.eviltester.com/styled/alerts/fake-alert-test.html")
    assert "Fake Alerts" in browser.title   
    try:
        fake_alert_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fakealert"))
        )
        fake_alert_button.click()
    except NoSuchElementException:
        pass
    sleep(5)
