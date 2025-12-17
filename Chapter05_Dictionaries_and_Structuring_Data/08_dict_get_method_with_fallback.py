cat = {"sound": "meow", "color": "brown", "size": "small", "age": 2}

cat_color = cat.get("color", "No Color") # -> (key, fallback value)
print(cat_color)

cat_height = cat.get("height", "No Height") # -> (key, fallback value)
print(cat_height)