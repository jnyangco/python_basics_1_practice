from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from instance_methods_page import ExampleHomePage


def main():
    # Optional: make Chrome a little more stable in automation runs
    options = Options()
    # options.add_argument("--headless=new")  # keep commented so you can SEE the browser

    # Create a DRIVER - OBJECT/INSTANCE
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Create a PAGE - OBJECT/INSTANCE
    page = ExampleHomePage(driver)

    page.open()
    heading_text = page.get_heading_text()
    print(f"Heading text: {heading_text}")

    # Instance method returning True/False (very test-like)
    # assert or if else method to verify text
    if page.is_heading_text_correct("Example Domains"):
        print("PASSED: Heading matches expected text")
    else:
        print("FAILED: Heading does NOT match expected text")

    driver.quit()


if __name__ == "__main__":
    main()