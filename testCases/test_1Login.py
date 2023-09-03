from time import sleep

import pytest
from self import self
from pages.loginPage import LoginPage
from selenium import webdriver

# driver = webdriver.Chrome()
class Test_Login():

    @pytest.fixture(autouse=True)
    def objects(self):
        self.lg = LoginPage(self.driver)

    def test_username(self):
        self.lg.username()
        assert self.driver.current_url == "http://devdreamcity.kolonizer.in/logi"

    def test_password(self):
        self.lg.password()

    def test_loginButton(self):
        self.lg.clickOnLoginButton()
