"""
Lab 7:

"""

def main():
    filename = "Lab07Q03_1.txt"
    print(get_biggest_difference(filename))
    print()

    filename = "Lab07Q03_2.txt"
    print(get_biggest_difference(filename))


def get_biggest_difference(filename):
    input_file = open(filename, "r")
    content = input_file.read()
    number_list = content.split()
    for index in range(len(number_list)):
        number_list[index] = int(number_list[index])
    result = max(number_list) - min(number_list)
    input_file.close()
    return result


main()








