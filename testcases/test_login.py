import pytest
from selenium import webdriver
from pageobjetct.LoginPage import Login
from testcases.conftest import setup
from utilities.Helper import get_row_value


class Test_Login_001:

    baseUrl="https://www.facebook.com/"
   # user ="demo"
    #passw="123"

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        current_title=self.driver.title
        print(current_title)
        if current_title=="Facebook":
            assert True
        else:
            assert False

    def test_loginuserandpass(self,setup):
        self.driver=setup

        self.driver.get(self.baseUrl)
        self.l = Login(self.driver)
        self.user, self.passw = get_row_value(3,1,3,2)
        self.l.setUserName(self.user)
        self.l.setPassword(self.passw)
        self.l.setLoginButton()



