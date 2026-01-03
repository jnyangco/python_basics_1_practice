# home_page.py → a page object that HAS-A WaitHelper and ElementHelper

from selenium.webdriver.common.by import By

class HomePage:
    """
    Page Object (NOT inheriting from BasePage)

    Composition:
    HomePage HAS-A driver
    HomePage HAS-A WaitHelper
    HomePage HAS-A ElementHelper
    """

    URL = "https://example.com"
    HEADING = (By.TAG_NAME, "h1")
    PARAGRAPH = (By.TAG_NAME, "p")


    def __init__(self, driver, wait_helper, element_helper):
        self.driver = driver
        self.wait = wait_helper
        self.elements = element_helper

    def open(self):
        self.driver.get(self.URL)

    def get_heading_text(self):
        # Use WaitHelper (composition)
        self.wait.wait_for_visible(self.HEADING)

        # Use ElementHelper (composition)
        return self.elements.get_text(self.HEADING)

    def get_paragraph_text(self):
        self.wait.wait_for_visible(self.PARAGRAPH)
        return self.elements.get_text(self.PARAGRAPH)