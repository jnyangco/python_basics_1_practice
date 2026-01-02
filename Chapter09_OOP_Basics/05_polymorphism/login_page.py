from base_page import BasePage

# CHILD CLASS
class LoginPage(BasePage):

    """
    CHILD CLASS

    It also OVERRIDES open() (polymorphism).
    """

    LOGIN_URL = "https://www.saucedemo.com/"

    def open(self):
        # Overriding the parent's open()
        self.driver.get(self.LOGIN_URL)

