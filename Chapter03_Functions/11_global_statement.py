def spam():
    global eggs
    eggs = "local eggs"

eggs = "new eggs"
spam()
print(eggs)
