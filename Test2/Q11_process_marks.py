def process_marks(filename):
    input_file = open(filename, "r")
    file_line_list = input_file.read().split()
    result_dict = {}
    for index in range(len(file_line_list)):
        comma_index = file_line_list[index].rfind(",")
        left_list = file_line_list[index][:comma_index].split(",")
        right_list = file_line_list[index][comma_index+1:].split(":")
        for index in range(len(right_list)):
            right_list[index] = int(right_list[index])
        for index in range(len(left_list)):
            if left_list[index] in result_dict:
                result_dict[left_list[index]] = result_dict[left_list[index]] + (right_list[index],)
            else:
                result_dict[left_list[index]] = (right_list[index],)
    for key in result_dict:
        result_dict[key] = list(result_dict[key])
        result_dict[key].sort()
        result_dict[key] = tuple(result_dict[key])
    return result_dict

def print_dict(score_dict):
    for key in score_dict:
        print(key,": ",score_dict[key],sep="")
    return








filename1 = "Input1.txt"
marks_dict = process_marks(filename1)
print_dict(marks_dict)