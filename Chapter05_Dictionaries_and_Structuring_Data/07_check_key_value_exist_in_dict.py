cat = {"sound": "meow", "color": "brown", "size": "small", "age": 2}

print("--------------------")
if "sizes" in cat.keys():
    print("True")
else:
    print("False")

print("--------------------")
if 2 in cat.values():
    print("True")
else:
    print("False")


print("--------------------")
if "sound" in cat:  # it will look for KEYS (NOT VALUES)
    print("True")
else:
    print("False")

print("--------------------")
if "sound" in cat.items():  # False
    print("True")
else:
    print("False")

