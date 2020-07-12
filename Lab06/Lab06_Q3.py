"""
Lab 6:

"""

def main():
    numbers_list = [31, 636, 2042, 40, 447]
    print(numbers_list)
    numbers_list2 = get_sorted_increased_decreased(numbers_list)
    print(numbers_list2)
    print()

    numbers_list = [11, 4559, 241, 12, 924]
    print(numbers_list)
    print(get_sorted_increased_decreased(numbers_list))
    print()

    numbers_list = [101, 45594, 1241, 9, 92]
    print(numbers_list)
    print(get_sorted_increased_decreased(numbers_list))


def get_sorted_increased_decreased(numbers_list):
    result = []
    for index in range(len(numbers_list)):
        if numbers_list[index] < 100:
            result.append(numbers_list[index] * 10)
        else:
            result.append(numbers_list[index] // 10)
        result.sort(reverse=True)
    return result



main()








