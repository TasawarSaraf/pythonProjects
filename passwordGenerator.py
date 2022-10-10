

import random
# this project is to generate a random password using python

lowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

upperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ["@", "#", "$", "%", "!", "^", "&", "*"]

passwordGenerator = ""


# want to make the password 15 characters long



for i in range(4):
     randomLetterIndex = random.randint(0, 25)
     randomDigitIndex = random.randint(0, 9)
     randomSymbolIndex = random.randint(0,7)

     lowercaseLetter = lowerCase[randomLetterIndex] 
     uppercaseLetter = upperCase[randomLetterIndex]
     number = digits[randomDigitIndex]
     symbol = symbols[randomSymbolIndex]


     passwordGenerator += lowercaseLetter
     passwordGenerator += uppercaseLetter
     passwordGenerator += symbol
     passwordGenerator += str(number)




print(passwordGenerator)