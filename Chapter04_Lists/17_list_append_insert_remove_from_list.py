pets = ["dog", "cat", "bird"]
print(pets)

print("-----------------------")
pets.append("rat")
print(pets)

print("-----------------------")
print("-----------------------")
del pets[-1]  # remove using index
print(pets)

print("-----------------------")
pets = ["dog", "cat", "bird"]
pets.__delitem__(0) # remove using index
print(pets)


print("-----------------------")
pets = ["dog", "cat", "bird"]
pets.remove("cat")
print(pets)

print("-----------------------")
letters = ["A", "B", "B", "C", "D"]
letters.remove("B")
print(letters)