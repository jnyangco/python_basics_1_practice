def spam():
    global eggs
    eggs = "changed global eggs value"

eggs = "outside eggs"
print(eggs)

spam()
print(eggs)