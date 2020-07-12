def split_digits(line):
    line_list = []
    for index in range(len(line)):
        line_list.append(int(line[index]))
    return line_list




print(split_digits('11155111'))
print(split_digits('11111111'))