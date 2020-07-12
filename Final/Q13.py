# def main():
#     a_list = [5, 7, 2]
#     do_something_a(a_list)
#     print("a_list:", a_list)
#
# def do_something_a(list1):
#     list2 = list1
#     to_consider = [1, 6]
#     for element in to_consider:
#         list2.insert(0, element)
#     list1.reverse()
#
# if __name__ == '__main__':
#     main()


def main():
    a_list = [5, 4]
    do_something_b(a_list)
    print("a_list:", a_list)

def do_something_b(list1):
    list2 = list1
    list1 = [4, 3]
    for element in [1, 5, 3]:
        if element not in list1:
            list1.append(element)
    list1 = list2

if __name__ == '__main__':
    main()