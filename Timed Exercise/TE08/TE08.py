"""
TimedQuiz 08
Author:
Date: May, 2020
This program creates a baby names lengths analysis.
"""
def main():
    filename = "2000TopNames.txt"
    names = get_list_of_names(filename)
    name_lengths_dict = create_name_lengths_dictionary(names)
    produce_name_lengths_report(name_lengths_dict)

def create_name_lengths_dictionary(names_list): 
    result = {}
    for index in range(len(names_list)):
        if len(names_list[index]) in result:
            result[len(names_list[index])] = result[len(names_list[index])] + 1
        else:
            result[len(names_list[index])] = 1
    return result

def produce_name_lengths_report(name_lengths_dict):
    print("Report")
    print("======")
    for element in sorted(name_lengths_dict.keys()):
        print("{} letter baby names: {} times".format(element, name_lengths_dict[element]))

def get_list_of_names(filename):
    input_files = open(filename, "r")
    result_list = input_files.read().split()
    input_files.close()
    return result_list

main()
