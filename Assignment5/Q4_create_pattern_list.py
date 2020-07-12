def split_digits(line):
    line_list = []
    for index in range(len(line)):
        line_list.append(int(line[index]))
    return line_list

def create_pattern_list(lines):
    lines_list = []
    for index in range(len(lines)):
        lines_list.append(split_digits(lines[index]))
    return lines_list









lines = ['11221222', '13221121', '14421441', '24412442', '11344221', '21444421', '22444432', '22412411']
print(create_pattern_list(lines))
lines = ['11111111', '11111111', '12222221', '22222222', '23422432', '22255222', '22122122', '22111122']
print(create_pattern_list(lines))