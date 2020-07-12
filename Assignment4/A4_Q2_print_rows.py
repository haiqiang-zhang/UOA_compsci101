""" Use this file to develop and test your Assignment 4 function 2"""

#--------------------------------------------------
# 2222222222222222222222222222222222222222222222222
# print_rows()
#--------------------------------------------------
def print_rows(row_dict):
    row_list = list(row_dict.items())
    row_list.sort()
    for index in range(len(row_list)):
        if row_list[index][1][0] >= 1 and row_list[index][1][1] >= 1:
            print("*"*min(row_list[index][1]), row_list[index][0].upper()*max(row_list[index][1]), "*"*min(row_list[index][1]), sep="", end="")
    return ()


def main():
    print_header(2, "print_rows()")
    print_rows({'a': (4, 3), 'c': (5, 0), 'b': (-2, 5)})
    print()

    print_rows({'d': (12, -3), 'c': (1, 2), 'b': (3, -4), 'f': (11, 6)})
    print()

    print_rows({'d': (6, -3), 'z': (1, 3), 'b': (3, 0), 's': (4, 6)})

#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()

