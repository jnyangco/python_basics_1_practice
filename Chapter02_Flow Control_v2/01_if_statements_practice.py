print("----------------------------------------")
username = "admin"
if username == "admin":
    print("Welcome, admin!")

password = ""
if password == "": # same with -> if not password
    print("Password cannot be empty!")

email = "john.doe@example.com"
if len(email) > 5:
    print("Email looks valid!")


# error_message = driver.find_element(By.ID, "error").text
# if error_message == "Invalid credentials":
#     print("Login failed!")
print("\n----------------------------------------")

is_logged_in = True
if is_logged_in:
    print("User accessed the dashboard")

is_subscribed = False
if is_subscribed:
    print("You have unlimited access")

print("\n----------------------------------------")
filename = "admin_report.pdf"
if filename.endswith(".pdf"):
    print("This is a pdf file")

print("\n----------------------------------------")
website = "https://google.com"
if website.startswith("https"):
    print("Secure connection")

print("\n----------------------------------------")
message = "Error: File not found"
if "Error" in message:
    print("An error occurred.")


print("\n=============== selenium hint ===============")
# current_url = driver.current_url
# if "login" in currect_url:
#     print("User is on login page")