def get_common_elements(list1, list2):
    combine_list = []
    for index in range(len(list1)):
        if list1[index] in list2:
            combine_list.append(list1[index])
    for index in range(len(list2)):
        if list2[index] in list1:
            combine_list.append(list2[index])
    index = 0
    while index <= len(combine_list) - 1:
        if combine_list[index] in combine_list[:index] or combine_list[index] in combine_list[index + 1:]:
            combine_list.pop(index)
        else:
            index += 1
    combine_list.sort()
    return combine_list
numbers1 = [3, 78, 785, 4, 99, 677, 23, 9]
numbers2 = [3, 2, 9, 4]
print(get_common_elements(numbers1, numbers2))
print(get_common_elements([3, 23, 99, 4], [4, 99, 7, 5, 23, 3]))
print(get_common_elements([], [3, 23, 77, 4]))