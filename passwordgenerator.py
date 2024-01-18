import random

print('Welcome to the Password Generator')
chars = 'ABCEDHIJKLMNOPQRSTUVWXYZabcefghjiklmnopqrstuvwxyz1234567890!*$%&/()='

number = input('Number of passwords: ')
number = int(number)

length = input('Length of passwords:  ')
length = int(length)

print('Here are your passwords:')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)