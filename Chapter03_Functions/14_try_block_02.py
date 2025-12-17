def division(num1, num2):
    return num1 / num2


try:
    print(division(4, 2))
    print(division(4, 0))
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


