""" Assignment 3 function 6"""

def main():
    print_header(6, "remove_triplets()")
    a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [6, 6, 6, 7, 6, 6, 6, 6, 6]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [6, 6, 6]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [1, 1, 1, 1]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
#--------------------------------------------------
# 6666666666666666666666666666666666666666666666666
# Remove triplets made up of three sequential
# identical elements
#--------------------------------------------------
def remove_triplets(a_list):
    index = 0
    result = []
    while index <= len(a_list)-1:
        if len(a_list)-1 - index >= 2:
            if a_list[index] == a_list[index + 1] and a_list[index + 1] == a_list[index + 2]:
                index = index + 3
            else:
                result.append(a_list[index])
                index += 1              
        else:
           result.append(a_list[index])
           index += 1
    for index in range(len(a_list)-1,-1,-1):
        a_list.pop(index)
    for index in range(len(result)):
        a_list.append(result[index])
    return()
            

#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
