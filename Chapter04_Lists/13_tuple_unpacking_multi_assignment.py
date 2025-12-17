
print("-------------------------")
# list -> tuple unpacking
list_pets = ["woofy", "catty", "birdy"]
dog, cat, bird = list_pets
print(dog)
print(cat)
print(bird)

print("-------------------------")
def get_user_info():
    name = "Alice"
    age = 20
    job = "Engineer"
    return name, age, job   # this will return a tuple -> ('Alice', 20, 'Engineer')

# print(get_user_info())
name, age, job = get_user_info() # tuple unpacking
print(f"Name: {name}, age: {age}, job: {job}")
