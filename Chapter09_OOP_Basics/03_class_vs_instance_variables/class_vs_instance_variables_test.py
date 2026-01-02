from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from class_vs_instance_variables_page import ExampleHomePage

def main():
    options = Options()
    # options.add_argument("--headless=new")  # keep commented so you can see the browser

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Create TWO page objects (two instances)
    page1 = ExampleHomePage(driver)
    page2 = ExampleHomePage(driver)

    # ✅ CLASS VARIABLES (shared)
    print(f"Class variable BASE_URL via Class: {ExampleHomePage.BASE_URL}")
    print(f"Class variable BASE_URL via page1: {page1.BASE_URL}")
    print(f"Class variable BASE_URL via page2: {page2.BASE_URL}")

    print("-------------------------------------")
    # Use instance methods (these rely on instance variable: self.driver)
    page1.open()
    heading_text = page1.get_heading_text()
    paragraph_text = page1.get_paragraph_text()
    print(f"Heading: {heading_text} ")
    print(f"Paragraph: {paragraph_text} ")

    # ✅ Change CLASS VARIABLE using the CLASS (affects ALL objects)
    ExampleHomePage.DEFAULT_TIMEOUT_SECONDS = 10
    print(f"Timeout via page1 after Class change: {page1.DEFAULT_TIMEOUT_SECONDS}")
    print(f"Timeout via page2 after Class change: {page2.DEFAULT_TIMEOUT_SECONDS}")

    print("-------------------------------------")
    # ⚠️ Show the "shadowing" trick (instance variable with same name as class variable)
    # This creates an INSTANCE variable ONLY on page1 -> does NOT change class variable
    page1.BASE_URL = "https://www.google.com"

    print(f"After page1.BASE_URL instance override:")
    print(f"page1.BASE_URL = {page1.BASE_URL}")
    print(f"page2.BASE_URL = {page2.BASE_URL}")
    print(f"ExampleHomePage.BASE_URL = {ExampleHomePage.BASE_URL}")

    driver.quit()

if __name__ == "__main__":
    main()