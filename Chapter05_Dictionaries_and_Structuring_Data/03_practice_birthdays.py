birthdays = {"Alice": "July 10", "Bob": "October 3", "Charlie": "March 30"}

while True:
    name = input("Enter name to check birthday: ")
    if name == "":
        print("System Exit...")
        break

    if name in birthdays:
        print(f"Found in the database. {name} birthday is {birthdays[name]}")
    else:
        print(f"{name} NOT found in the database.")
        save_birthday = input("Enter birthday to save in the database: ")
        birthdays[name] = save_birthday
        print("Saved!")