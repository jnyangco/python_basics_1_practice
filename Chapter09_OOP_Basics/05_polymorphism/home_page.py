from base_page import BasePage

# CHILD CLASS
class HomePage(BasePage):

    """
    CHILD CLASS

    It also OVERRIDES open() (polymorphism).
    """

    HOME_URL = "https://opensource-demo.orangehrmlive.com/"

    def open(self):
        # Overriding the parent's open()
        self.driver.get(self.HOME_URL)

