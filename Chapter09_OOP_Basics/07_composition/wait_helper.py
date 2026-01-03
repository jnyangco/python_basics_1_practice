# wait_helper.py → a helper that HAS-A driver and waits for elements

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:
    """
    Helper class (component)

    Composition:
    WaitHelper HAS-A driver (stored as self.driver)
    """

    def __init__(self, driver, timeout_seconds=5):
        self.driver = driver
        self.timeout_seconds = timeout_seconds

    def wait_for_visible(self, locator):
        """
        Wait until the element is visible and return the WebElement.
        """
        wait = WebDriverWait(self.driver, self.timeout_seconds)
        return wait.until(EC.visibility_of_element_located(locator))


