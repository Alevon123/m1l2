import random


symbolb = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = int(input("Введите желаемую длину пароля: "))
degenerated_password = ""

for i in range(password):
    random_2 = random.choice(symbolb)
    degenerated_password += random_2

print("Ваш пасворд:", degenerated_password)

