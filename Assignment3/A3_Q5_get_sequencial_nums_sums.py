""" Assignment 3 function 5"""

def main():
    print_header(5, "get_sequencial_nums_sums()")
    list1 = [3, 3, 2, 3, 4, 3]
    print(list1, end = " => ")
    print(get_sequencial_nums_sums(list1))
    print()

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list1, end = " => ")
    print(get_sequencial_nums_sums(list1))
    print()

    list1 = [3]
    print(list1, end = " => ")
    print(get_sequencial_nums_sums(list1))
    print(get_sequencial_nums_sums([]))

#--------------------------------------------------
# 5555555555555555555555555555555555555555555555555
# Returns a list with the totals of each pair of
# of elements of the parameter list.
#--------------------------------------------------
def get_sequencial_nums_sums(list1):
    sum_list = []
    if len(list1)%2 == 0:
        for index in range(0,len(list1),2):
            sum_list.append(list1[index]+list1[index+1])
    else:
        for index in range(0,len(list1)-1,2):
            sum_list.append(list1[index]+list1[index+1])
        sum_list.append(list1[-1])
    return sum_list
#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
