"""
Lab 7:

"""

def main():
    number_repeated = get_number_of_unique_repeats("Lab07Q05_1.txt")
    print(number_repeated)
    print()

    print(get_number_of_unique_repeats("Lab07Q05_2.txt"))
    print()

    print(get_number_of_unique_repeats("Lab07Q05_3.txt"))


def get_number_of_unique_repeats(filename):
    input_file = open(filename, "r")
    list_name = input_file.read().split()
    list_repeat = []
    count_repeat = 0
    for index0 in range(len(list_name)):
        for index1 in range(index0+1, len(list_name)):
            if list_name[index0] == list_name[index1]:
                list_repeat.append(list_name[index0])
                break
    index2 = 0
    while index2 <= len(list_repeat)-1:
        index3 = index2+1
        while index3 <= len(list_repeat)-1:
            if list_repeat[index2] == list_repeat[index3]:
                list_repeat.pop(index3)
            index3 += 1
        index2 += 1
    input_file.close()
    return len(list_repeat)

main()








