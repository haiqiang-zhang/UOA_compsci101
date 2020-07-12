import random

def replace_letter(a_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    random_string_index = random.randrange(len(a_string))
    random_alphabet_index = random.randrange(len(alphabet))
    while a_string[random_string_index] == alphabet[random_alphabet_index]:
        random_alphabet_index = random.randrange(len(alphabet))
    after_replace_word = alphabet[random_alphabet_index]
    result = a_string[:random_string_index] + after_replace_word + a_string[random_string_index + 1:]
    return result


print(replace_letter("awesome"))