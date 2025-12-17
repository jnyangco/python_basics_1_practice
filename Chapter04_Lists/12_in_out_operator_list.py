list_names = ["Alice", "Bob", "Charlie"]
string_name = "John Doe"
dict_names = {"name1": "Alice", "name2": "Bob", "name3": "Charlie"}

print("------------------------")
print("Alice" in list_names)
print("Bob" not in list_names)
print("Dough" in list_names)

print("------------------------")
print("Doe" in string_name)
print("Doe" not in string_name)
print("Alice" not in string_name)

print("------------------------")
print("name1" in dict_names)
print("name3" in dict_names)
print("name4" in dict_names)
print("name5" not in dict_names)

print("------------------------")
if "Bob" in list_names:
    print("\"Bob\" is in the records!")
else:
    print("\"Bob\" is NOT in the records!")