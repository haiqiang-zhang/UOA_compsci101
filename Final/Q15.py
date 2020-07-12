def main():
    data_dict = {"Balrog": [73, 67, 47, 44], "Bison": [63, 54, 25], "Chun Li": [95, 89, 72, 66], "Ken": [100, 75, 65, 55], "Ryu": [100, 95, 80, 70]}
    filename = "Output.txt"
    write_to_file(filename, data_dict, 4)


def write_to_file(filename, data_dict, max_length):
    key_list = list(data_dict.keys())
    key_list.sort()
    output_stream = open(filename, "w")
    for key in key_list:
        output_stream.write(key + ": ")
        values = data_dict[key]
        values.sort()
        if len(values) > max_length:
            values = values[len(values) - max_length:]
        for i in range(len(values) - 1, -1, -1):
            if i == 0:
                output_stream.write(str(values[i]) + "\n")
            else:
                output_stream.write(str(values[i]) + ", ")
    output_stream.close()


main()
