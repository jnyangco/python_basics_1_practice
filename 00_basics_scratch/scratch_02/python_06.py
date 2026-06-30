import random

# generate secret number
secret_number = random.randint(1, 10)

# create for loop with 5 tries
for i in range(1, 6):
    guess_number = int(input("Guess the number: "))

    if guess_number < secret_number:
        print("Your guess is less than the secret number")
    elif guess_number > secret_number:
        print("Your guess is greater than the secret number")
    elif guess_number == secret_number:
        print("You got it!")
        break
    else:
        print("Invalid input")

    if i == 5:
        print("Game over! Try again...")
        break