""" Use this file to develop and test your Assignment 4 function 4"""

#--------------------------------------------------
# 4444444444444444444444444444444444444444444444444
# get_last_three_letters_dict(text)
#--------------------------------------------------
def get_last_three_letters_dict(text):
    text_list = text.split()
    text_three_list = []
    text_dict = {}
    for index in range(len(text_list)):
        text_list[index] = text_list[index].lower()
    for index in range(len(text_list)):
        if len(text_list[index]) > 2:
            text_three_list.append(text_list[index][-3:])
    for index in range(len(text_three_list)):
        if text_three_list[index] in text_dict:
            text_dict[text_three_list[index]] += 1
        else:
            text_dict[text_three_list[index]] = 1
    return text_dict



def main():
    print_header(4, "get_last_three_letters_dict()")
    text = 'nubile singer linger finger juvenile tiger turnstile mobile tile'
    a_dict = get_last_three_letters_dict(text)
    remove_less_than_2(a_dict)
    print_dict_in_key_order(a_dict)
    print()

    text = 'west best worst first tapping snapping in a pest the straining singing forest living'
    a_dict = get_last_three_letters_dict(text)
    remove_less_than_2(a_dict)
    print_dict_in_key_order(a_dict)
    print()

    text = 'to do or a at'
    a_dict = get_last_three_letters_dict(text)
    remove_less_than_2(a_dict)
    print_dict_in_key_order(a_dict)

#--------------------------------------------------
# Two helper functions
#--------------------------------------------------
def print_dict_in_key_order(a_dict):
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        print(key, ":", a_dict[key])

def remove_less_than_2(a_dict):
    all_keys = list(a_dict.keys())
    for key in all_keys:
        if a_dict[key] == 1:
            del a_dict[key]
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
