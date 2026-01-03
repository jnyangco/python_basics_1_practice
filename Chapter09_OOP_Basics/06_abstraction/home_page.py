from base_page import BasePage

class HomePage(BasePage):
    """
    CHILD CLASS

    Must implement open(), because BasePage requires it.
    """

    # Constants
    HOME_URL = "https://example.com"

    def open(self):
        # Implementing the abstract method
        self.driver.get(self.HOME_URL)