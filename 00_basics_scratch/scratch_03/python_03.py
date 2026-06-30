def get_message(number):
    if number == 1:
        return "Good Morning"
    elif number == 2:
        return "Good Afternoon"
    elif number == 3:
        return "Good Evening"
    else:
        return None

try:
    number = int(input("Enter a number: "))
    print(get_message(number))
except ValueError:
    print("Please enter a valid number")