from abc import ABC, abstractmethod


class BasePage:
    """
    ABSTRACT BASE CLASS for all pages.

    Key idea:
    - You should NOT create BasePage() directly.
    - Child pages MUST implement open().
    """
    # Constructor
    def __init__(self, driver):
        # INSTANCE VARIABLE
        # Every page object needs a driver
        self.driver = driver


    @abstractmethod
    def open(self):
        """
       ABSTRACT METHOD (contract)
       Every child page MUST implement open().
       """
        # pass

    # NOTE: it can be write in one line without comments below -> def open(self): pass


    # Regular (non-abstract) shared helper method
    def get_title(self):
        return self.driver.title


