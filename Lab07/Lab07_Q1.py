"""
Lab 7:

"""

def main():
    a_tuple = (-3, 6, 9, 4, 5)
    print(get_small_middle_large(a_tuple))
    print()

    print(get_small_middle_large((2,)))
    print()

    print(get_small_middle_large((2, -5)))
    print()

    print(get_small_middle_large((6, 7, 0, 3, 2, 8)))

def get_small_middle_large(a_tuple):
    a_list = list(a_tuple)
    a_list.sort()
    if len(a_tuple) > 2:
        middle_index = len(a_tuple) // 2
        return (a_list[0], a_list[middle_index], a_list[-1])
    elif len(a_tuple) == 2:
        return (a_list[0], a_list[1])
    else:
        return a_tuple





main()








