def process_file(line):
    input_file = open(line, "r")
    file_list = input_file.read().split()
    return file_list








print(process_file("steve.txt"))
print(process_file("steve_palette.txt"))