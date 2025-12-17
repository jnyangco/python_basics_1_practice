names = ["Alice", "bird", "Bob", "Charlie"]
numbers = [2, 4, 1, 0, 7]

print("------------------------------------------")
names.sort()
numbers.sort()
print(numbers)
print(names)


print("------------------------------------------")
names.sort(reverse=True)
print(names)

print("------------------------------------------")
names.reverse()
print(names)


print("------------------------------------------")
print("------------------------------------------")
sorted_names = sorted(names, key=str.lower)
print(sorted_names)


