def main():
    print_slices("magical", 2, 5)
    print_slices("singing", 1, 4)
    print_slices("01234567", 4, 1)
    print_slices("lucky", 0, 3)
    print_slices("good", 3, 0)


def print_slices(word, index1, index2):
    word = word.upper()
    if index1 < index2:
        first_part = word[0:index1]
        second_part = word[index1:index2]
        third_part = word[index2:]
    else:
        first_part = word[0:index2]
        second_part = word[index2:index1]
        third_part = word[index1:]
    print(first_part, second_part, third_part)
    return()



main()