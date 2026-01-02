# PARENT CLASS
class BasePage:
    """
    PARENT CLASS (Base / Super class)

    This class contains common code for all pages.
    Child pages will INHERIT from this.
    """

    # CLASS VARIABLE
    BASE_URL = "https://example.com"

    def __init__(self, driver):
        # Instance Variable (per object)
        self.driver = driver

    def open(self):
        """
        This is an instance method in the parent class.

        Child classes can OVERRIDE this to open a different URL.
        """
        self.driver.get(self.BASE_URL)