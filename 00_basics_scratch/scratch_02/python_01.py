
while True:
    name = input('Enter your name: ')
    if name != 'John':
        print('Incorrect username. Try again...')
        continue

    password = input('Enter your password: ')
    if password != 'Password@1234':
        print('Incorrect password. Try again...')
        continue
    break

print('Access Granted!')