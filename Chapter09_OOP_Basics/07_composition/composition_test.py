# composition_test.py → creates driver + helpers, injects them into the page, runs the test
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from wait_helper import WaitHelper
from wait_helper_fast import WaitHelperFast
from element_helper import ElementHelper
from home_page import HomePage


def main():
    options = Options()
    # options.add_argument("--headless=new")  # keep commented so you can see the browser

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Create helper objects (components)
    # wait = WaitHelper(driver, timeout_seconds=5)
    wait = WaitHelperFast(driver)
    elements = ElementHelper(driver)

    # Inject helpers into the page object (composition + dependency injection)
    home = HomePage(driver, wait, elements)
    home.open()
    time.sleep(2)

    heading_text = home.get_heading_text()
    paragraph_text = home.get_paragraph_text()

    print(f"Heading: {heading_text}")
    print(f"Paragraph: {paragraph_text}")

    driver.quit()

if __name__ == "__main__":
    main()