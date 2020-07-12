"""
Lab 5:
"""

def main():
    print([117, -241, -171, 112, 317, 290, 77, 394], "- ", end = "")
    result = contains_only_3_digit_numbers([117, -241, -171, 112, 317, 290, 77, 394])
    print(result)
    print([-491, -375, -65, -348], "- ", end = "")
    print(contains_only_3_digit_numbers([-491, -375, -65, -348]))
    print([830, 466, -641, 820, -437, 875, -677], "- ", end = "")
    print(contains_only_3_digit_numbers([830, 466, -641, 820, -437, 875, -677]))

def contains_only_3_digit_numbers(numbers):
    for index in range(len(numbers)):
        numbers_abs = abs(numbers[index])
        if len(str(numbers_abs)) != 3:
            result = False
            break
        else:
            result = True
    return result

main()








