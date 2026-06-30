import sys

while True:
    answer = input("Enter option [continue] [exit]: ")
    if answer.lower() == "exit":
        print("System exit!")
        sys.exit()
