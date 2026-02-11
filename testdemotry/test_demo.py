
from selenium import webdriver
from testdemotry import *

class Test_Login_002:
      # baseUrl = "https://www.facebook.com/"
       for r in range(ass):

    def test_homePageTitle(self):
        self.driver=webdriver.Edge()
        self.driver.get("https://www.facebook.com")

        self.driver.find_element(By.NAME, "email").send_keys()

