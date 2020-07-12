import math

def get_lines_from_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.read().split()
    return lines



def main():
    lines = get_lines_from_file('basic.txt')
    print(lines)


main()
