cat = {"sound": "meow", "color": "brown", "size": "small", "age": 2}

print("====================================================================")
print(cat["color"])
cat["color"] = "black"
print(cat["color"])

cat["height"] = 4       # this will add/override the value even if the KEY is EXISTING
print(cat)

cat["height"] = 7       # this will add/override the value even if the KEY is EXISTING
print(cat)

print(cat["height"])

print("====================================================================")
cat.setdefault("weight", 3)
print(cat)
cat.setdefault("height", 10)  # if KEY is EXISTING - it will NOT UPDATE the Value -> IF EXIST RETURN CURRENT VALUE
print("Height (existing value): {}".format(cat.setdefault("height", 10))) # IF EXIST RETURN CURRENT VALUE
print(cat)
