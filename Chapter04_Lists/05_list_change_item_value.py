list_animals = ["dog", "cat", "bird", "elephant", "giraffe"]

# print("--------------")
# for i in range(len(list_animals)):
#     print(list_animals[i])

print("--------------")
for animal in list_animals:
    print(animal)

print("--------------")
list_animals[0] = "woofy!"
list_animals[1] = "meowy!"

for animal in list_animals:
    print(animal)

