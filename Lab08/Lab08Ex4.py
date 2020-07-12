"""
Lab 8 Ex 4
Author:
Date: May, 2020
This program reads in a file of baby names and
prints a list of baby names by initial letter
"""
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    baby_name_dictionary = create_baby_names_dictionary(names)
    display_baby_names(baby_name_dictionary)

def get_filename_from_user():
    filename = input("Enter a filename: ")
    return filename
    
def get_list_of_names(filename):
    input_file = open(filename, "r")
    file_list = input_file.read().split()
    return file_list

def create_baby_names_dictionary(names_list): 
    names_dict = {}
    for index in range(len(names_list)):
        initial = names_list[index][0]
        if initial in names_dict:
            names_dict[initial].append(names_list[index])
        else:
            names_dict[initial] = [names_list[index]]
    return names_dict

def display_baby_names(baby_names_dict):
    sort_list = []
    for key in baby_names_dict:
        str_baby_names_dict = str()
        baby_names_dict[key].sort()
        for index in range(len(baby_names_dict[key])):
            if index == 0:
                str_baby_names_dict = baby_names_dict[key][index]
            else:
                str_baby_names_dict = str_baby_names_dict + " " + baby_names_dict[key][index]
        sort_list_element = key + ": " + str_baby_names_dict
        sort_list.append(sort_list_element)
    sort_list.sort()
    for index in range(len(sort_list)):
        print(sort_list[index])
    return()

main()
