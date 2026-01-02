from selenium.webdriver.common.by import By

class ExampleHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://example.com"

    def open(self):
        self.driver.get(self.url)

    def get_heading_text(self):
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        return heading.text

    def is_heading_text_correct(self, expected_text):
        actual_text = self.get_heading_text()
        return actual_text == expected_text


