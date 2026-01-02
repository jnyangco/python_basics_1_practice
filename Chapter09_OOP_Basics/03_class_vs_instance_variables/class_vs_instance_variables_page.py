from selenium.webdriver.common.by import By


class ExampleHomePage:
    """
    Page Object CLASS (blueprint)

    This class demonstrates:
    - CLASS VARIABLES: shared by ALL page objects
    - INSTANCE VARIABLES: unique per page object instance
    """

    # ✅ CLASS VARIABLES (shared by ALL instances/objects)
    BASE_URL = "https://example.com"
    DEFAULT_TIMEOUT_SECONDS = 5

    # CLASS LEVEL CONSTANTS - ALL CAPITAL
    # Locators are often good as class variables (same for every object)
    HEADING = (By.TAG_NAME, "h1")
    PARAGRAPH = (By.TAG_NAME, "p")



    # CONSTRUCTOR
    def __init__(self, driver):
        # ✅ INSTANCE VARIABLE (belongs to ONE object)
        # Each page object has its own driver (browser controller)
        self.driver = driver


    # ✅ INSTANCE METHODS (uses instance variable self.driver + class variable BASE_URL)
    def open(self):
        self.driver.get(self.BASE_URL)

    def get_heading_text(self):
        heading = self.driver.find_element(*self.HEADING)
        return heading.text

    def get_paragraph_text(self):
        paragraph = self.driver.find_element(*self.PARAGRAPH)
        return paragraph.text

    def is_heading_text_correct(self, expected_text):
        return self.get_heading_text() == expected_text



