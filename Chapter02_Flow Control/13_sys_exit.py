import sys

while True:
    user_input = input("Enter option [Continue] [Exit]: ")
    if user_input.lower() == "exit":
        print("System exit!")
        sys.exit()

    print(f"You typed {user_input}")