# base_page.py → parent class with common code + a default open()
# login_page.py → child class overrides open()
# home_page.py → child class overrides open()
# polymorphism_test.py → one test that calls page.open() without caring which page it is (that’s polymorphism)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from home_page import HomePage
from login_page import LoginPage
from base_page import BasePage



def main():
    options = Options()
    # options.add_argument("--headless=new")  # keep commented so you can see the browser

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    home = HomePage(driver)
    login = LoginPage(driver)
    base = BasePage(driver)

    # List of different page objects (different classes)
    pages = [home, login, base]

    # SAME method call -> different behavior depending on object type
    for page in pages:
        print(f"Opening: {page.__class__.__name__}")
        page.open()
        time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    main()