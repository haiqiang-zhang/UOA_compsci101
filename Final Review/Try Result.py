# def main():
#     a_list = []
#     b_list = []
#     a = 5
#     a_list.append(a)
#     b = first(a)
#     b_list.append(b)
#     print("4.", b)
#     b = second(b)
#     b_list.append(b)
#     print("5.", b)
#     print("main:", a_list, b_list)
# def first(a):
#     a_list = []
#     b_list = []
#     a_list.append(a)
#     b = 3
#     b_list.append(b)
#     print("1.", a)
#     print("first:", a_list, b_list)
#     return a * b
#
# def second(a):
#     a_list = []
#     b_list = []
#     a_list.append(a)
#     print("2.", a - 5)
#     a = third(a // 4)
#     a_list.append(a)
#     print("second:", a_list, b_list)
#     return a % 7
#
# def third(a):
#     a_list = []
#     b_list = []
#     a_list.append(a)
#     print("3.", a)
#     print("third:", a_list, b_list)
#     return a + 4
#
# main()
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
# def main():
#     a = 5
#     b = first(a)
#     print("4.", b)
#     b = second(b)
#     print("5.", b)
#
# def first(a):
#     b = 3
#     print("1.", a)
#     return a * b
#
# def second(a):
#     print("2.", a - 5)
#     a = third(a // 4)
#     return a % 7
#
# def third(a):
#     print("3.", a)
#     return a + 4
#
# main()
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def main():
    print("A", end = " ")
    do1()

def do1():
    do3()
    print("B", end = " ")
    do2()

def do2():
    print("C", end = " ")

def do3():
    do2()
    print("D", end = " ")

main()