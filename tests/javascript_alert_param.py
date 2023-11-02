import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("alert_label",[
    ("JavaScript Alerts"),
    ("Confirm box:"),
    ("Prompt box:")
])
def test_javascript_alert(browser:webdriver,alert_label):
    browser.get("https://www.lambdatest.com/selenium-playground/javascript-alert-box-demo")

    print(alert_label)
    element_with_text = browser.find_element(By.XPATH, "//*[text()='"+alert_label+"']")
    element_with_text.find_element(By.CSS_SELECTOR, '.btn').click()
    sleep(5)
    browser.switch_to.alert.accept()