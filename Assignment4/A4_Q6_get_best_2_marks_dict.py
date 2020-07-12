""" Use this file to develop and test your Assignment 4 function 6"""

#--------------------------------------------------
# 6666666666666666666666666666666666666666666666666
# get_best_2_marks_dict()
#--------------------------------------------------
def get_best_2_marks_dict(filename):
    input_file = open(filename, "r")
    file_list = input_file.readlines()
    score_dict = {}
    for index in range(len(file_list)):
        temp_list = file_list[index].split()
        score_dict[temp_list[0]] = temp_list[1:]
    for key in score_dict:
        for index in range(len(score_dict[key])):
            score_dict[key][index] = int(score_dict[key][index])
        score_dict[key].sort()
        score_dict[key] = tuple(score_dict[key][-2:])
    return score_dict


def main():
    print_header(6, "get_best_2_marks_dict()")
    the_dict = get_best_2_marks_dict("NamesMarks1.txt")
    print_dict_in_key_order(the_dict)
    print()

    the_dict = get_best_2_marks_dict("NamesMarks2.txt")
    print_dict_in_key_order(the_dict)

#--------------------------------------------------
# A helper function
#--------------------------------------------------
def print_dict_in_key_order(a_dict):
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        print(key, ":", a_dict[key])
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
