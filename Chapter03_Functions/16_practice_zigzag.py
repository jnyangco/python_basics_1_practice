import time, sys

indent = 0
indent_increase = True

while True:
    print(" " * indent, end="")
    print("**********")


    if indent_increase:
        indent += 1

        if indent == 20:
            indent_increase = False
    else:
        indent -= 1
        if indent == 0:
            indent_increase = True

    time.sleep(0.04)

