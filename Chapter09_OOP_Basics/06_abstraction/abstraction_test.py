import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from home_page import HomePage
from login_page import LoginPage

def main():
    options = Options()
    # options.add_argument("--headless=new")  # keep commented so you can see the browser

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Create child page objects
    home = HomePage(driver)
    login = LoginPage(driver)

    # Put them into a list typed as "BasePage contract"
    pages = [home, login]

    # BONUS -> this is POLYMORPHISM (multiple forms)
    # We only rely on the contract:
    # every page MUST have open()
    for page in pages:
        print(f"Opening: {page.__class__.__name__}")
        page.open()
        time.sleep(2)
        print(f"Title: {page.get_title()}")
        print("--------------------------")

    driver.quit()


if __name__ == "__main__":
    main()