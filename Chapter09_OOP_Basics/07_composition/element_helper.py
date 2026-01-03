# element_helper.py → a helper that HAS-A driver and finds/clicks/gets text

class ElementHelper:
    """
    Helper class (component)

    Composition:
    ElementHelper HAS-A driver (stored as self.driver)
    """

    def __init__(self, driver):
        self.driver = driver

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text


