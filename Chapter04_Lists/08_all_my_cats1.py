# cat1 = input("Enter the name of Cat 1: ")
# cat2 = input("Enter the name of Cat 2: ")
# print(cat1 + " " + cat2)

list_cat = []
for i in range(3):
    cat = input("Enter the name of Cat {}: ".format(i))
    # list_cat += [cat]
    list_cat.append(cat)

print("Cat names are: ")
for cat in list_cat:
    print(cat)