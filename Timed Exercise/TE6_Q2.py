def remove_3_digit_numbers(numbers_list):
    index = 0
    sync_index = 0
    while index <= sync_index:
        if len(str(numbers_list[index])) == 3:
            numbers_list.pop(index)
        else:
            index += 1
        sync_index = len(numbers_list) - 1
    return()



numbers_list = [117, 41, 171, 112, 317, 290, 77, 39]
remove_3_digit_numbers(numbers_list)
print(numbers_list)