counter = 0

while counter < 5:
    print(counter)
    counter += 1


name = ''
while name != 'Alice':
    name = input('Enter your name: ')
    if name == 'Alice':
        break

print('Program exit...')
