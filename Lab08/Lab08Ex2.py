"""
Lab 8 Ex 2
Author:
Date: May, 2020
This program creates a baby names dictionary 
"""
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    baby_names_dictionary = create_baby_names_dict(names)
    display_baby_names(baby_names_dictionary)

def get_filename_from_user():
    filename = input("Enter a filename: ")
    return filename

def get_list_of_names(filename):
    input_file = open(filename, "r")
    file_list = input_file.read().split()
    return file_list

def create_baby_names_dict(names_list):
    names_dict = {}
    for index in range(len(names_list)):
        initial = names_list[index][0]
        names_dict[initial] = names_list[index]
    return names_dict

def display_baby_names(baby_names_dictionary):
    for key in baby_names_dictionary:
        print(key, baby_names_dictionary[key], end=", ")

main()
