def a():
    print("a() starts")
    b()
    c()
    print("a() ends")

def b():
    print("b() starts")
    print("b() ends")

def c():
    print("c() starts")
    print("c() ends")


a() # this will call a() + b() + c()