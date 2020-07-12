def sum_over(a_list_of_lists, target):
    sum_result = 0
    for index1 in range(len(a_list_of_lists)):
        for index2 in range(len(a_list_of_lists[index1])):
            if a_list_of_lists[index1][index2] > target:
                sum_result = sum_result + a_list_of_lists[index1][index2]
    return sum_result








the_list = [[2, 4, 16, 80, 27], [1, 4, 120, 18, 7], [20, 14, 70, 8, 130]]
print(sum_over(the_list, 50))
the_list = [[2, 4, 16, 80, 27], [1, 4, 120, 18, 7], [20, 14, 70, 8, 130]]
print(sum_over(the_list, 100))