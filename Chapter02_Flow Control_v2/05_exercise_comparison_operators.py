password = "Pass@1231234"
password_strength = 0


if len(password) >= 8:
    print("Length is good")
    password_strength += 1

if len(password) >= 12:
    print("Excellent length")
    password_strength += 1

if password != password.lower():
    print("Has an uppercase")
    password_strength += 1

if "123" in password:
    print("Contains numbers")
    password_strength += 1


print(f"Score: {password_strength}")
if password_strength == 0:
    print("Password strength: Very Weak")
elif password_strength == 1:
    print("Password strength: Weak")
elif password_strength == 2:
    print("Password strength: Medium")
elif password_strength == 3:
    print("Password strength: Strong")
elif password_strength >= 4:
    print("Password strength: Very Strong")




# ==============================================
# Selenium Hint
# if driver.findElement(By.ID, "header"):
#     print("Element Found!")
#
# if driver.title == "header":
#     print("Correct Title!")