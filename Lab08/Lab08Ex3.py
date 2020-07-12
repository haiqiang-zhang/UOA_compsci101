"""
Lab 8 Ex 3
Author:
Date: May, 2020
This program produces a summary of the top 10 baby names
"""
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    name_count_dictionary = create_names_count_dictionary(names)
    produce_name_counts_report(name_count_dictionary)

def get_filename_from_user():
    filename = input("Enter a filename: ")
    return filename

def get_list_of_names(filename):
    input_file = open(filename, "r")
    file_list = input_file.read().split()
    return file_list

def create_names_count_dictionary(names_list):
    baby_count_dict = {}
    for index in range(len(names_list)):
        if names_list[index] in baby_count_dict:
            baby_count_dict[names_list[index]] += 1
        else:
            baby_count_dict[names_list[index]] = int(1)
    return baby_count_dict

def produce_name_counts_report(name_counts_dict):
    print("Report")
    print("======")
    sort_list = []
    for key in name_counts_dict:
        sort_list_element = key + " appears " + str(name_counts_dict[key]) + " times"
        sort_list.append(sort_list_element)
    sort_list.sort()
    for index in range(len(sort_list)):
        print(sort_list[index])


main()
