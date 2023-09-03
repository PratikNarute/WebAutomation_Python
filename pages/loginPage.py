from selenium import webdriver

import utility.excel
from utility import  peformActions



class LoginPage():
    emailId = "//input[@id='mat-input-0']"
    passWord = "//input[@id='mat-input-1']"
    loginButton = "//span[text()='login']/parent::button"

    def __init__(self, driver):
        self.driver = driver

    def username(self):
        print(utility.excel.importData("Sheet", 1,1))
        peformActions.sendActon(self,self.driver,utility.excel.importData("Sheet", 1,1),self.emailId)


    def password(self):
        peformActions.sendActon(self, self.driver, utility.excel.importData("Sheet", 1,2), self.passWord, )

    def clickOnLoginButton(self):
        peformActions.clickAction(self,self.driver,self.loginButton)

    def login(self):
        peformActions.sendActon(self, self.driver, "pratik@kolonizer.com", self.emailId)
        peformActions.sendActon(self, self.driver, "123", self.passWord, )
        peformActions.clickAction(self,self.driver,self.loginButton)
