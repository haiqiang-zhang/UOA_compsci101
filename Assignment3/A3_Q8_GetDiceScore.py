"""Assignment 3 function 8"""

def main():
    print_header(8, "get_dice_score()")
    print("1:", get_dice_score([5, 3, 2, 5, 4, 5, 6, 4, 3]))
    print("2:", get_dice_score([3, 4, 1, 5, 3, 1, 4, 6]))
    print("3:", get_dice_score([5, 3, 2, 2, 6, 4, 5, 1, 4]))
    print("4:", get_dice_score([2, 1, 1, 1, 2, 3, 3, 1, 3, 2]))
    print("5:", get_dice_score([3, 4, 1, 5, 2, 1, 5, 1, 2, 3, 4, 6]))
    print("6:", get_dice_score([]))
    list1 = [5, 3, 2, 6, 4, 5, 1, 4, 1, 2, 6, 4]
    print("8:", get_dice_score(list1), end=" - ")
    print(list1)
#--------------------------------------------------
# 8888888888888888888888888888888888888888888888888
# Score a hand of random dice throws
#--------------------------------------------------
def get_dice_score(list_of_dice):
    result = 0
    number_list = []
    number_list_number = 0
    for number in range(1,7):
        for index in range(len(list_of_dice)):
            if list_of_dice[index] == number:
                number_list_number = number_list_number + 1
        number_list.append(number_list_number)
        number_list_number = 0
    while True:
        if 0 in number_list:
            number_list = number_list[:number_list.index(0)]
        number_list.reverse()
        if len(number_list) != 0:
            min_number = min(number_list)
            min_index = number_list.index(min_number)
            for index in range(1,len(number_list)+1):
                result = result + index*min_number
            for index in range(len(number_list)):
                number_list[index] = number_list[index]-min_number
            number_list.reverse()
        else:
            break
    return result

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
