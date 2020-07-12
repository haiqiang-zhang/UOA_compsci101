"""
Lab 7:

"""

def main():
    number_same = get_length_same("Lab07Q04_1.txt", "Lab07Q04_2.txt")
    print(number_same)
    print()

    print(get_length_same("Lab07Q04_3.txt", "Lab07Q04_4.txt"))
    print()

    print(get_length_same("Lab07Q04_5.txt", "Lab07Q04_6.txt"))
    
def get_length_same(filename1, filename2):
    input_file1 = open(filename1, "r")
    input_file2 = open(filename2, "r")
    content1 = input_file1.read()
    content2 = input_file2.read()
    range_index = min(len(content1), len(content2))
    result = 0
    for index in range(range_index):
        if content1[index] == content2[index]:
            result += 1
        elif content1[index] != content2[index]:
            break
    input_file1.close()
    input_file2.close()
    return result



main()








