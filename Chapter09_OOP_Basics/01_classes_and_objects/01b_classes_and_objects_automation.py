from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# This is a CLASS (blueprint)
class ExampleHomePage:

    # This is the CONSTRUCTOR
    # It runs automatically when we create an object like:
    # page = ExampleHomePage(driver)
    def __init__(self, driver):
        # INSTANCE VARIABLE:
        # This "driver" belongs to THIS specific page object
        # It stores the browser controller inside the object
        self.driver = driver

        self.url = "https://example.com"


    # This is a METHOD (a function inside a class)
    # It lets the object DO something: open the page
    def open(self):
        self.driver.get(self.url)

    # Another method: read the heading text on the page
    def get_heading_text(self):
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        return heading.text

    def get_paragraph_text(self):
        paragraph = self.driver.find_element(By.TAG_NAME, "p")
        return paragraph.text




def main():
    # Create a browser (Chrome)
    driver = webdriver.Chrome()

    driver.maximize_window()

    # CREATE AN OBJECT (instance) of the ExampleHomePage class
    # This is the key "classes & objects" moment in Selenium
    page = ExampleHomePage(driver)

    # Use the object (call its methods)
    page.open()
    time.sleep(2)

    heading_text = page.get_heading_text()
    print(f"Heading text: {heading_text}")

    paragraph_text = page.get_paragraph_text()
    print(f"Paragraph text: {paragraph_text}")

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    main()