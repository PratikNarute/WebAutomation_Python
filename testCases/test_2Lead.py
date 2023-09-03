from time import sleep

import pytest
from self import self

from pages.lead import Lead
from pages.loginPage import LoginPage



# @pytest.mark.usefixtures("open_tearDown")
class Test_Lead():

    @pytest.fixture(autouse=True)
    def objects(self):
        self.lg = LoginPage(self.driver)
        self.l = Lead(self.driver)

    def test_Create_interested_lead(self):
        self.lg.login()
        sleep(2)
        self.l.clickOnAddLeadButton()
        self.l.clickOnProjectDropdown()
        self.l.selectProjectList()
        sleep(5)
        self.driver.close()

