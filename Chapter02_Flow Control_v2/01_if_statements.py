print("=============== example ===============")
age = 20

if age >= 18:
    print("You are an adult!")

print("This always run...")


print("\n=============== practice ===============")
temperature = 9

if temperature > 30:
    print("It's hot outside!")

if temperature < 10:
    print("It's cold outside!")

print("Have a nice day!")



print("\n=============== selenium hint ===============")
status_code = 404
if status_code == 200:
    print("Page load successfully!")

if status_code == 404:
    print("Page not found! Taking screenshot...")
    # driver.take_screenshot("img_error_404.png")