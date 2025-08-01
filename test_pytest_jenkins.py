from selenium import webdriver
import pytest
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    path = Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=path)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def credentials():
    return [
        ('standard_user','secret_sauce'),
        ('locked_out_user','secret_sauce'),
        ('problem_user','secret_sauce')
    ]

@pytest.mark.parametrize("username,password", credentials())

def test_login(username,password):
    myusername = driver.find_element(By.ID, "user-name")
    myusername.send_keys(username)

    time.sleep(3)

    mypassword = driver.find_element(By.ID, "password")
    mypassword.send_keys(password)
    time.sleep(3)

    loginbutton = driver.find_element(By.ID, 'login-button')
    loginbutton.click()
    time.sleep(12)