""" Use this file to develop and test your Assignment 4 function 1"""

#--------------------------------------------------
# 1111111111111111111111111111111111111111111111111
# get_dictionary_from_file()
#--------------------------------------------------
def get_dictionary_from_file(filename):
    input_file = open(filename, "r")
    file_list = input_file.readlines()
    result_dict = {}
    for index in range(len(file_list)):
        result_dict[file_list[index][:file_list[index].find(":")].strip()] = file_list[index][file_list[index].find(":")+1:].strip()
    return result_dict



def main():
    print_header(1, "test_get_dictionary_from_file()")
    the_dict = get_dictionary_from_file("WordsAndMeanings1.txt")
    for word in ["lickspittle", "allegator", "lickety-split"]:
        if word in the_dict:
            print(word, "=", the_dict[word])
    print()

    the_dict = get_dictionary_from_file("WordsAndMeanings2.txt")
    for word in ["ranivorous", "cat", "rigmarole"]:
        if word in the_dict:
            print(word, "=", the_dict[word])
    print()

    the_dict = get_dictionary_from_file("WordsAndMeanings3.txt")
    for word in ["gastromancy", "allegator", "gazump"]:
        if word in the_dict:
            print(word, "=", the_dict[word])

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
