def change_negatives_to_zero(numbers_list):
    for index in range(len(numbers_list)):
        if numbers_list[index] < 0:
            numbers_list.pop(index)
            numbers_list.insert(index, 0)
    return()


numbers_list = [117, -241, -171, 112, 317, 290, 77, 394]
change_negatives_to_zero(numbers_list)
print(numbers_list)