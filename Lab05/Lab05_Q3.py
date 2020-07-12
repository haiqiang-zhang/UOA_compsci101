"""
Lab 5:
"""

def main():
    print("[51, -55, 56, 23, 23, 54] - ", end = "")
    even_non_negatives = get_list_of_non_negative_evens([51, -55, 56, 23, 23, 54])
    print(even_non_negatives)
    print("[46, 26, 24, -44, -20] - ", end = "")
    print(get_list_of_non_negative_evens([46, 26, 24, -44, -20]))
    print("[51, 13, -23, -54] - ", end = "")
    print(get_list_of_non_negative_evens([51, 13, -23, -54]))

def get_list_of_non_negative_evens(numbers_list):
    my_list = []
    for index in range(len(numbers_list)):
        if numbers_list[index] >= 0 and numbers_list[index] % 2 == 0:
            my_list.append(numbers_list[index])
    return my_list
            
    
    

main()








