from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(2) 
    
    def login(self,username,password):
        self.driver.find_element(*self.username_field).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.password_field).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.login_button).click()
        time.sleep(3)