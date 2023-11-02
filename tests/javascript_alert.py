import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_javascript_alert(browser:webdriver):
    browser.get("https://www.lambdatest.com/selenium-playground/javascript-alert-box-demo")
    alert_labels= [
        'JavaScript Alerts',
        'Confirm box:',
        'Prompt box:'
    ]
    for alert in alert_labels:
        print(alert)
        element_with_text = browser.find_element(By.XPATH, "//*[text()='"+alert+"']")
        element_with_text.find_element(By.CSS_SELECTOR, '.btn').click()
        sleep(5)
        browser.switch_to.alert.accept()