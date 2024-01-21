import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

count = int(input('Введи длину пароля'))

password = ''

for i in range(count):
    password += random.choice(symbols)

print(password)