name = ''
while not name:
    name = input('Enter your name: ')


total_guests = int(input('Enter your total guests: '))
if not total_guests:
    print(f'Total guests is {total_guests}')
else:
    print(f'Invalid total guests')