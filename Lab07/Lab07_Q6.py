"""
Lab 7:

"""
def main():
    message = ("For this question you are required to submit\n" +
            "ONE line of text, the line numbered 100 from the\n" +
            "output file created by this program.")
    print(message)

    write_without_blank_lines("Lab07Q06_in.txt", "Lab07Q06_out.txt")


def write_without_blank_lines(filename_in, filename_out):
    input_file = open(filename_in, "r")
    output_file = open(filename_out, "w")
    line_list = input_file.readlines()
    line_number = 1
    for index in range(len(line_list)):
        if line_list[index] != '\n':
            write = str(line_number) + ". " + line_list[index]
            line_number += 1
            output_file.write(write)
    input_file.close()
    output_file.close()
    return()

    print(line_list)


main()








