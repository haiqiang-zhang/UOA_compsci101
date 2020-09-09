import random





consonants = "bcdfghjklmnprstvwz"
vowels =     "aeiouaeiouaeiouaei"
random.seed(45)

number_of_star = 16
star = "*" * number_of_star
number1 = random.randrange(len(consonants))
Number1 = consonants[number1]
consonants = consonants[:number1] + consonants[number1+1:]

Number2 = vowels[number1]
vowels = vowels[:number1] + vowels[number1+1:]
number3 = random.randrange(len(consonants))
Number3 = consonants[number3]
consonants = consonants[:number3] + consonants[number3+1:]

Number4 = vowels[number3]
vowels = vowels[:number3] + vowels[number3+1:]
number5 = random.randrange(len(consonants))
Number5 = consonants[number5]

Number6 = vowels[number5]

print()
print(star)
print(star)
print("     ", Number1, Number2, Number3, Number4, Number5, Number6, "     ",sep="")
print(star)
print(star)
print()