print("\n=============== example ===============")
username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Admin login successfully")
elif username == "admin" and password != "admin123":
    print("Incorrect password")
elif username != "admin":
    print("User not found")
else:
    print("Unknown error")

print("\n=============== practice ===============")
num1 = 10
num2 = 5
operation = "multiply"

if operation == "add":
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
elif operation == "subtract":
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
elif operation == "multiply":
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
elif operation == "divide":
    if num2 == 0:
        print("Error: cannot divide by zero!")
    else:
        print(f"Division: {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operation")
