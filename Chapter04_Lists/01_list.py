list_numbers = [2, 4, 3, 8, 10]
list_strings = ["cat", "dog", "bird", "rat", "elephant"]
list_data = ["hello", 3.1415, True, False, 42]



print("====================================")
print(list_numbers)
print(f"Size: {len(list_numbers)}")
print(f"First item: {list_numbers[0]}")
print(f"Last item: {list_numbers[len(list_numbers) - 1]}")


print("====================================")
print(list_strings)
print(list_numbers[0])
print(len(list_strings))

# Sort by alphabet
list_strings.sort()
print(list_strings)

print(list_strings.count("cat"))
print(list_strings.index("rat"))
list_strings.append("giraffe")
print(list_strings)

print("====================================")
pop1 = list_strings.pop()
print(pop1)
print(list_strings)

pop2 = list_strings.pop(2)
print(pop2)
print(list_strings)

print("====================================")
print(list_strings[-1])