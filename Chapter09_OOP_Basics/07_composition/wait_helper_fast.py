

class WaitHelperFast:
    """
    Alternative wait helper.

    Same PURPOSE as WaitHelper,
    but NO real waiting (fast / dummy implementation).
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visible(self, locator):
        # No waiting — just find immediately
        return self.driver.find_element(*locator)