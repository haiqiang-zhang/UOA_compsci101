""" Use this file to develop and test your Assignment 4 function 3"""

#--------------------------------------------------
#33333333333333333333333333333333333333333333333333
# print_highest_frequency_keys()
#--------------------------------------------------
def print_highest_frequency_keys(frequency_dict, key_length):
    dict_list = list(frequency_dict.items())
    length_list = []
    result_list = []
    for index in range(len(dict_list)):
        if len(dict_list[index][0]) == key_length:
            length_list.append(dict_list[index])
    highest_frequency = 0
    for index in range(len(length_list)):
        if length_list[index][1] > highest_frequency:
            highest_frequency = length_list[index][1]
    for index in range(len(length_list)):
        if length_list[index][1] == highest_frequency:
            result_list.append(length_list[index][0])
    result_list.sort()
    print(key_length, "letter keys:", result_list, highest_frequency)
    return()








def main():
    print_header(3, "print_highest_frequency_keys()")
    word_frequencies = {"fish":9,  "parrot":8,  "frog":9,  "cat":9,  "stork":1,  "dog":4, "bat":9,  "rat":3}
    print_highest_frequency_keys(word_frequencies, 3)
    print_highest_frequency_keys(word_frequencies, 4)
    print_highest_frequency_keys(word_frequencies, 7)

#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
