from utility import peformActions


class Lead():
    addLead_button = "//span[text()='ADD LEAD']/ancestor::button"
    project_dropdown = "//mat-select[@formcontrolname='project_id']"
    project_list = "//mat-option//span"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAddLeadButton(self):
        peformActions.clickAction(self,self.driver, self.addLead_button)

    def clickOnProjectDropdown(self):
        peformActions.clickAction(self, self.driver, self.project_dropdown, )

    def selectProjectList(self):
        peformActions.clickAction(self,self.driver,self.project_list)