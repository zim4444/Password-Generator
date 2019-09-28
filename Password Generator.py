import random

chars = '`1234567890-=qwertyuiop[]\asdfghjkl;zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

number = input('Number of Passwords? - ')
number = int(number)

length = input('Password Legnth? - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
    
