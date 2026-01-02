from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from home_page import HomePage


def main():
    options = Options()
    # options.add_argument("--headless=new")  # keep commented so you can see the browser

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Create a HomePage object (child class object)
    # It inherits BasePage methods automatically.
    homepage = HomePage(driver)  # BasePage requires "driver" argument/parameter

    # This method is INHERITED from BasePage
    homepage.open_base_url()

    # These methods are from HomePage (child class)
    heading_text = homepage.get_heading_text()
    paragraph_text = homepage.get_paragraph_text()

    print(f"Heading: {heading_text}")
    print(f"Paragraph: {paragraph_text}")

    print("---------------------------------------")

    # Use a child method that checks heading
    if homepage.is_heading_correct("Example Domain"):
        print("PASSED: Heading text is correct")
    else:
        print("FAILED: Heading text NOT correct")

    if homepage.is_paragraph_correct("This domain is for use in documentation examples without needing permission. "
                                   "Avoid use in operations."):
        print("PASSED: Paragraph text is correct")
    else:
        print("FAILED: Paragraph text is NOT correct")


    driver.quit()



if __name__ == "__main__":
    main()