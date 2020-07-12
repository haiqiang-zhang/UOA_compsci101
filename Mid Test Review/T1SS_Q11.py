def main():
    sort_four_nums(1, 2, 3, 4)
    sort_four_nums(9, 8, 7, 6)
    sort_four_nums(11, 12, 11, 13)


def sort_four_nums(num1, num2, num3, num4):
    first = min(num1, num2, num3, num4)
    fourth = max(num1, num2, num3, num4)
    middle1 = min(max(num1, num2), max(num1, num3), max(num1, num4), max(num2, num3), max(num2, num4), max(num3, num4))
    middle2 = max(min(num1, num2), min(num1, num3), min(num1, num4), min(num2, num3), min(num2, num4), min(num3, num4))
    print(first, middle1, middle2, fourth)
    return()


















main()