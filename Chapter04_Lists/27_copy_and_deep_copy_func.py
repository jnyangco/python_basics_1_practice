import copy

spam = ["dog", "cat", "bird"]
# cheese = spam
cheese = copy.copy(spam)
spam[2] = "giraffe"

print(spam)
print(cheese)