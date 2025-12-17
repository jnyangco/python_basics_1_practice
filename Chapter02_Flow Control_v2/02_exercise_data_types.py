# user_role = guest or member or admin
user_role = "guest"
if user_role == "admin":
    print("Full access granted")

if user_role == "member":
    print("Limited access granted")

if user_role == "guest":
    print("Please register")


is_verified = True
if is_verified:
    print("Account is verified")


product_code = "11223344"
if len(product_code) == 8:
    print("Valid product code")


url = "https://example.com"
if "https" in url:
    print("Secure connection")

discount_percentage = 55.0
if discount_percentage >= 50.0:
    print("Big Sale!")


print("\n----------------------------------------")
is_verified = False
if not is_verified: # if not true
    print("Please verify your account")

user_input = "ADMIN"
if user_input.lower() == "admin":
    print("Full access granted")

url = "https://secure-payment.com"
if "https" in url and "secure" in url:
    print("Very secured website")

print("\n=============== practice ===============")
product_code = "11478234"
if product_code.startswith("11"):
    print("Product is from Electronics category")

discount_percentage = 50
if discount_percentage >= 40 and discount_percentage <= 60:
    print("Big Discount!")


print("\n=============== selenium hint ===============")
# page_title = driver.title
# if page_title == "Login - MyApp":
#     print("On login page, entering credentials...")
#
# button_enabled = driver.find_element(By.ID, "submit").is_enabled()
# if button_enabled:
#     print("Button is clickable")
#
# entered_phone = "12345678"
# if len(entered_phone) == 8:
#     print("Valid phone number format")
#
# current_url = driver.current_url
# if "dashboard" in current_url:
#     print("Successfully navigated to dashboard")
#
# response_time = 2.5
# if response_time >= 3.0:
#     print("Page is loading slowly")