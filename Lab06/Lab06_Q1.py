"""
Lab 6:

"""

def main():
    numbers1 = [1, 4, 6, 2, 9, 8]
    numbers2 = [4, 0, 8, 1, 9, 7, 1]
    print(numbers1)
    print(numbers2)
    print(have_same_start_total(numbers1, numbers2))
    print()

    numbers1 = [1, 4, 5, 2, 9, 8]
    numbers2 = [4, 0, 8, 1, 9, 7, 1]
    print(numbers1)
    print(numbers2)
    print(have_same_start_total(numbers1, numbers2))
    print()

    numbers1 = [1, 4, 5]
    numbers2 = [4, 0, 8, 1, 9, 7, 1]
    print(numbers1)
    print(numbers2)
    print(have_same_start_total(numbers1, numbers2))

def have_same_start_total(list1, list2):
    if len(list1) >= 4 and len(list2) >= 4:
        sum1 = 0
        sum2 = 0
        for index in range(0, 4):
            sum1 = sum1 + list1[index]
            sum2 = sum2 + list2[index]
        if sum1 == sum2:
            return True
        else:
            return False
    else:
        return False

main()








