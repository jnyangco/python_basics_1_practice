from selenium.webdriver.common.by import By
from base_page import BasePage


class HomePage(BasePage):
    """
    CHILD CLASS (Derived / Sub class)

    HomePage INHERITS from BasePage:
    - It automatically gets: __init__, open, open_base_URL, get_text, click, etc.
    """

    # Class variables for locators are common (shared, constant)
    HEADING = (By.TAG_NAME, "h1")
    PARAGRAPH = (By.TAG_NAME, "p")

    # We do NOT need to write __init__ here because we can inherit it.
    # BasePage.__init__(driver) will run when we create HomePage(driver).


    # Page-specific instance method (uses inherited get_text)
    def get_heading_text(self):
        return self.get_text(self.HEADING)

    # Page-specific instance method
    def get_paragraph_text(self):
        return self.get_text(self.PARAGRAPH)


    # Page-specific "check" method -> TRUE OR FALSE
    def is_heading_correct(self, expected_text):
        return self.get_heading_text() == expected_text

    def is_paragraph_correct(self, expected_text):
        return self.get_paragraph_text() == expected_text