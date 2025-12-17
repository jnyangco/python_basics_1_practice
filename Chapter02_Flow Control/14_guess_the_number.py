import random

secret_number = random.randint(1, 10)
for i in range(1, 6):
    guess_number = int(input("Guess the number: "))
    if guess_number < secret_number:
        print("Your guess number is less than the secret number")
    elif guess_number > secret_number:
        print("Your guess number is greather than the secret number")
    elif guess_number == secret_number:
        print("You got it! The secret number is {}".format(secret_number))
        break

    if i == 5:
        print("Game over! Try again!")
        break