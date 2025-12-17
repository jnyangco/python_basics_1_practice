# username = John
# password = swordfish

while True:
    username = input('Enter username: ')
    if username != 'John':
        print('Incorrect username. Try again...')
        continue

    password = input('Enter password: ')
    if password != 'swordfish':
        print('Incorrect password. Try again...')
        continue
    break

print('Access Granted!')


