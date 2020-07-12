def remove_all_repeats(numbers_list):
    index = 0
    while index <= len(numbers_list)-1:
        if numbers_list[index] in numbers_list[:index] or numbers_list[index] in numbers_list[index+1:]:
            numbers_list.pop(index)
        else:
            index += 1
    numbers_list.sort()
    return



numbers = [3, 71, 71, 3, 99, 3, 67, 88]
remove_all_repeats(numbers)
print(numbers)
numbers = [71, 71, 71, 71, 71, 71, 71, 71, 71, 71]
remove_all_repeats(numbers)
print(numbers)
numbers = [9, 71, 71, 9, 71, 9]
remove_all_repeats(numbers)
print(numbers)