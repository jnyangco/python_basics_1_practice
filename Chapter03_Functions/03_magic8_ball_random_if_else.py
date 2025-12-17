# create a function to get answer
def get_message(answer_number):
    if answer_number == 1:
        return "Hello There!"
    elif answer_number == 2:
        return "Good Morning!"
    elif answer_number == 3:
        return "Have a nice day!"
    elif answer_number == 4:
        return "Good evening!"
    else:
        return "Invalid answer!"

answer = int(input("Enter a number to reveal the message: "))
message = get_message(answer)
print(message)
















