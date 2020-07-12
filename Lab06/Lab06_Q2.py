"""
Lab 6:

"""

def main():
    numbers = [9, 0, 2, 5, 6, 4, 5]
    print(numbers)
    swap_elements(numbers, 2, 4)
    print(numbers)
    print()

    numbers = [9, 0, 9, 5, 6, 6, 5]
    print(numbers)
    swap_elements(numbers, 9, 6)
    print(numbers)
    print()

    numbers = [9, 8, 11, 5, 6, 7, 5]
    print(numbers)
    swap_elements(numbers, 6, 4)
    print(numbers)

def swap_elements(numbers_list, number1, number2):
    index1 = 0
    if number1 in numbers_list and number2 in numbers_list:
        if numbers_list.index(number1) < numbers_list.index(number2):
            while index1 <= len(numbers_list)-1:
                if numbers_list[index1] == number1:
                    numbers_list.pop(index1)
                    numbers_list.insert(index1, number2)
                    index1 += 1
                    break
                index1 += 1
            while index1 <= len(numbers_list)-1:
                if numbers_list[index1] == number2:
                    numbers_list.pop(index1)
                    numbers_list.insert(index1, number1)
                    break
                index1 += 1
        else:
            while index1 <= len(numbers_list)-1:
                if numbers_list[index1] == number2:
                    numbers_list.pop(index1)
                    numbers_list.insert(index1, number1)
                    index1 += 1
                    break
                index1 += 1
            while index1 <= len(numbers_list)-1:
                if numbers_list[index1] == number1:
                    numbers_list.pop(index1)
                    numbers_list.insert(index1, number2)
                    break
                index1 += 1

    return()


main()








