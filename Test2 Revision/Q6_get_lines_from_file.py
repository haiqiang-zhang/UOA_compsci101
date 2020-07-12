def get_lines_from_file(filename):
    input_file = open(filename, "r")
    result_lines = input_file.read().split()
    return result_lines





lines = get_lines_from_file('basic.txt')
print(lines)