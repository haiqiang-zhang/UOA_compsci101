def get_last_name_in_file(filename):
    input_file = open(filename, "r")
    file_list = input_file.read().split()
    return file_list[-1]