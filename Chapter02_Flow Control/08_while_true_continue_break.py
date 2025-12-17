
username = ''
password = ''


while True:
    username = input('Enter username: ')
    if username != 'John':
        print('Username not found. Try again...')
        continue

    password = input('Enter password: ')
    if password == 'Password@1':
        break   # jump out of the loop
    print('Incorrect password. Try again to enter username and password...')


print('Access Granted!')
