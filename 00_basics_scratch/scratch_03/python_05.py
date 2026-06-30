def a():
    print("A Starts")
    b()
    print("A Ends")

def b():
    print("B Starts")
    c()
    print("B Ends")

def c():
    print("C Starts")
    print("C Ends")

a()