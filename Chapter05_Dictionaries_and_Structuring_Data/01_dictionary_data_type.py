cat = {"sound": "meow", "color": "brown", "size": "small", "age": 2}
employee = {1048873: "Alice", 2989361: "Bob"}

print(cat["sound"])
print(cat["age"])
# print(cat["height"]) # KeyError: 'height'


print(employee[1048873])
print(employee[2989361])
# print(employee[1234567]) # KeyError: 1234567