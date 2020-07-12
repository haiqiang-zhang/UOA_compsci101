""" Use this file to develop and test your Assignment 4 function 7"""

#--------------------------------------------------
# 7777777777777777777777777777777777777777777777777
# get_next_words_dict()
#--------------------------------------------------
def get_next_words_dict(text):
    text_dict = {}
    text_list = text.split()
    for index in range(len(text_list)):
        text_list[index] = text_list[index].lower()
    for index in range(len(text_list)):
        if text_list[index] in text_dict:
            if index != len(text_list)-1:
                if text_list[index+1] not in text_dict[text_list[index]]:
                    text_dict[text_list[index]].append(text_list[index+1])
            else:
                text_dict[text_list[index]].append('')
        else:
            if index != len(text_list)-1:
                text_dict[text_list[index]] = [text_list[index+1]]
            else:
                text_dict[text_list[index]] = ['']
    for key in text_dict:
        text_dict[key].sort()
    return text_dict



def main():
    print_header(7, "get_next_words_dict()")
    text = 'Easy come easy go go easy go easy'
    next_words_dict = get_next_words_dict(text)
    print_dict_in_key_order(next_words_dict)
    print()

    text = 'happy joy happy happy joy joy'
    next_words_dict = get_next_words_dict(text)
    print_dict_in_key_order(next_words_dict)

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
