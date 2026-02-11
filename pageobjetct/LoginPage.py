
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    username_id = "email"
    password_name= "pass"
    login_xpath = "//button[@name='login']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def setLoginButton(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()