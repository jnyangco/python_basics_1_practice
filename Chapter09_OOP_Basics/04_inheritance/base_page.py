from selenium.webdriver.common.by import By


class BasePage:
    """
    PARENT CLASS (Base / Super class)

    This class holds code that is COMMON for many pages.
    Child pages will INHERIT everything here.
    """

    # CLASS VARIABLE (shared by all pages that inherit BasePage)
    BASE_URL = "https://example.com"

    # CONSTRUCTOR
    def __init__(self, driver):
        # INSTANCE VARIABLE (each page object has its own driver reference)
        self.driver = driver


    # INSTANCE METHOD: open any url
    def open(self, url):
        self.driver.get(url)

    # INSTANCE METHOD: open the default BASE_URL
    def open_base_url(self):
        self.driver.get(self.BASE_URL)

    # INSTANCE METHOD: get text of an element using a locator tuple
    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    # INSTANCE METHOD: click an element (we won't use it yet, but it's common)
    def click(self, locator):
        self.driver.find_element(*locator).click()


