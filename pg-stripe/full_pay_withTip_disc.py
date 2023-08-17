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
    location = ('https://app-staging.qlub.cloud/qr/ae/SezaiStripeDiscount/3/_/_/5f762ade4e')
    driver.get(location)
    sleep(10)

    # fetchOrder
    driver.find_element(By.XPATH, '//span[@class="wrapper"]/span').click()
    sleep(10)

    # ScrollDownPage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)

    # AddTip
    driver.find_element(By.XPATH, '//*[@id="tip_5"]/div').click()
    sleep(4)

    # Enter Card Number,Expiry Date, CVC
    driver.switch_to.frame(driver.find_element(By.XPATH,"(//iframe)[3]"))
    driver.find_element(By.XPATH,'//*[@id="Field-numberInput"]').send_keys("4242424242424242")
    driver.find_element(By.XPATH,'//*[@id="Field-expiryInput"]').send_keys("1130")
    driver.find_element(By.XPATH,'//*[@id="Field-cvcInput"]').send_keys("100")
    driver.switch_to.default_content()
    sleep(5)

    # Click On Pay Now
    driver.find_element(By.XPATH, '//span[normalize-space()="Pay Now"]').click()
    sleep(15)

    driver.quit()
    print('Successfull Payment')