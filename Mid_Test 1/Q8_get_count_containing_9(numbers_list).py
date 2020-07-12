def get_count_containing_9(numbers_list):
    count = 0
    for index in range(len(numbers_list)):
        if "9" in str(numbers_list[index]):
            count += 1
    return count


count_contain_9 = get_count_containing_9([393, 6369, 2042, 40, 9447])
print(count_contain_9)
print(get_count_containing_9([191, 45594, 1241, 9, 929]))
print(get_count_containing_9([465, 383, 282]))