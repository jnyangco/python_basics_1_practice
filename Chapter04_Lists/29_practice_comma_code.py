
def print_list_with_comma(list_values):
    for i in range(len(list_values)):
        if i < (len(list_values) - 2):
            print(list_values[i], end=", ")
        elif i < (len(list_values) - 1):
            print(list_values[i], end=" ")
        else:
            print(f"and {list_values[i]}")


spam = ['apples', 'bananas', 'tofu', 'cats', 'hello', 2, 4]
print_list_with_comma(spam)

