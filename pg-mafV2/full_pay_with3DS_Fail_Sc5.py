from asyncore import loop
#from http.client import ACCEPTED
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
def test_qr():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    location = ('https://app-staging.qlub.cloud/qr/ae/dummyMAFV2Sezai/7/_/_/ef811fb4a1')
    driver.get(location)
    sleep(10)

  # fetchOrder
    driver.find_element(By.XPATH, '//span[@class="wrapper"]/span').click()
    sleep(10)

    # Enter Card Number
    driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys("4242424242424242")
    sleep(2)
    # Enter Expiry Date
    driver.find_element(By.ID,'cardExpiry').send_keys("1031")
    sleep(2)
    # Enter CVC
    driver.find_element(By.NAME,'securityCode').send_keys("123")
    sleep(2)

    # ScrollDownPage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)

    # Click On Pay Now
    driver.find_element(By.CLASS_NAME, 'mafpay-default-card-submit').click()
    sleep(30)
    

    # Switch3DSpageClickOptions
    driver.switch_to.frame(driver.find_element(By.ID, 'simulatorFrame'))
    driver.find_element(By.XPATH, '//*[@id="selectAuthResult"]').click()
    driver.switch_to.default_content()
    sleep(5)

    # SelectOption1
    driver.switch_to.frame(driver.find_element(By.ID, 'simulatorFrame'))
    driver.find_element(By.XPATH, '//*[@id="selectAuthResult"]/option[6]').click()
    driver.switch_to.default_content()
    sleep(5)

    # ClickSubmit
    driver.switch_to.frame(driver.find_element(By.ID, 'simulatorFrame'))
    driver.find_element(By.XPATH, '//*[@id="ContainerContent"]/form/div[2]/button').click()
    driver.switch_to.default_content()
    sleep(15)

    driver.quit()
    print('Successfull Payment')






