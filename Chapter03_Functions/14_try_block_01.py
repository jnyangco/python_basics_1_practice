def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        # by default - it will return None

result = division(4, 2)
print(result)

result = division(4, 3)
print(result)

result = division(4, 0)
print(result)