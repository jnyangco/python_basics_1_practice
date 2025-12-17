import pprint

message = "Hello World"

dict_letters = {}

for i in range(len(message)):
    dict_letters.setdefault(i, message[i])

print(dict_letters)
print(len(dict_letters))

print(list(dict_letters)) # print keys only (convert to list)