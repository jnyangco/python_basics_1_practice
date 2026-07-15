def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero.")

result = division(4, 2)
print(result)

result = division(10, 0)
print(result)