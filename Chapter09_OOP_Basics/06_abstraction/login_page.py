from base_page import BasePage

class LoginPage(BasePage):
    """
    CHILD CLASS

    Must implement open().
    """

    # Constants
    LOGIN_URL = "https://www.saucedemo.com"

    def open(self):
        # Implementing the abstract methodf
        self.driver.get(self.LOGIN_URL)
