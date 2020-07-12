def has_exactly_2_of_each(a_list):
    if len(a_list) != 0:
        frequency_dict = {}
        for index in range(len(a_list)):
            if a_list[index] in frequency_dict:
                frequency_dict[a_list[index]] += 1
            else:
                frequency_dict[a_list[index]] = 1
        for key in frequency_dict:
            if frequency_dict[key] == 2:
                result = True
            else:
                result = False
                break
    else:
        result = True
    return result








numbers = [3, 78, 78, 3, 99, 67, 67, 99]
print(has_exactly_2_of_each(numbers))
print(has_exactly_2_of_each([9, 9, 9]))
print(has_exactly_2_of_each([3, 9, 9, 9, 9, 3]))
print(has_exactly_2_of_each([]))
