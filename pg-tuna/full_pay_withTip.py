from asyncore import loop
#from http.client import ACCEPTED
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

def test_tuna():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    location = ('https://app-staging.qlub.cloud/qr/br/dummyTunaSezai/4/_/_/37b61f25bb')
    driver.get(location)
    sleep(9)

    #fetchOrder
    driver.find_element(By.XPATH,'//span[@class="wrapper"]/span').click()
    sleep(10)

    # ScrollDownPage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)

    # AddTip
    driver.find_element(By.XPATH, '//*[@id="tip_5"]/div').click()
    sleep(4)

    #EnterCardInformations
    #Card HolderName
    driver.find_element(By.ID,':r2:').send_keys('Captured')
    sleep(3)
    #CardNumber
    driver.find_element(By.ID,':r3:').send_keys('5555555555554444')
    sleep(3)
    #ExpiryDate
    driver.find_element(By.ID,':r4:').send_keys('1128')
    sleep(3)
    #CVV
    driver.find_element(By.ID,':r5:').send_keys('222')
    sleep(5)

    #ClickOnPayNow
    driver.find_element(By.ID,'tuna-card-pay-button').click()
    sleep(15)

    driver.quit()
    print('Successfull Payment')
