print("\n=============== practice - nested if else ===============")
age = 20
has_license = False

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first before you can drive!")
else:
    print("You are too young to drive")