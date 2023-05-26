import random

letters = ["a", "b", "c", "d"]
digits = [1, 2, 3, 4]
symbol = ["!", "@", "#", "$"]
character = (letters + digits + symbol)
print(character)
password_letters_Length = int(input("What length of letters is best for you, folk!!! "))
password_digits_Length = int(input("What length of digits is best for you, folk!!! "))
password_symbols_Length = int(input("What length of symbols is best for you, folk!!! "))

newPassword = []
for x in range(password_letters_Length):
    newPassword.append(random.choice(letters))
for x in range(password_digits_Length):
    newPassword.append(random.choice(digits))
for x in range(password_symbols_Length):
    newPassword.append(random.choice(symbol))

finalPassword = "".join(map(str, newPassword))
#print("\n This is your new secret: ", finalPassword)
#random.shuffle(finalPassword)
print("\n This is your new secret: ", finalPassword)






