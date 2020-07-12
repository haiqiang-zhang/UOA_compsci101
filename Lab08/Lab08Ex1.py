"""
Lab 8 Ex 1
Author:
Date: May, 2020
This program prints a baby boy/girl name 
"""
def main():
    baby_boy_names_dictionary = {'A': 'Alex', 'B': 'Benjamin', 'C': 'Connor', 'D': 'Daniel', 'E': 'Ethan', 'F': 'Finn', 'G': 'George', 'H': 'Hunter', 'I': 'Isaac', 'J': 'Joshua', 'K': 'Kingston', 'L': 'Liam', 'M': 'Max', 'N': 'Noah', 'O': 'Oliver', 'P': 'Phoenix', 'Q': 'Quinn', 'R': 'Riley', 'S': 'Samuel', 'T': 'Thomas', 'U': 'Ute', 'V': 'Victor', 'W': 'William', 'X': 'Xavier', 'Y': 'Yukio', 'Z': 'Zachary'}
    baby_girl_names_dictionary = {'A': 'Abby', 'B': 'Bella', 'C': 'Charlotte', 'D': 'Daisy', 'E': 'Ella', 'F': 'Faith', 'G': 'Grace', 'H': 'Hannah', 'I': 'Isabella', 'J': 'Jade', 'K': 'Kate', 'L': 'Lily', 'M': 'Maddison', 'N': 'Natalie', 'O': 'Olivia', 'P': 'Phoebe', 'Q': 'Q', 'R': 'Rebecca', 'S': 'Samantha', 'T': 'Tayla', 'U': 'Ute', 'V': 'Violet', 'W': 'Willa', 'X': 'Xena', 'Y': 'Yuki', 'Z': 'Zoe'}
    letter = get_letter_from_user()
    print_baby_name(letter, baby_boy_names_dictionary)
    print_baby_name(letter, baby_girl_names_dictionary)

def get_letter_from_user():
    input_word = input("Enter a letter: ")
    input_word = input_word.upper()
    return input_word

def print_baby_name(letter, baby_names_dictionary):
    baby_name = baby_names_dictionary[letter]
    print("Baby name :", baby_name)
    return()

main()
