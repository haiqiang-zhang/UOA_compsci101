def get_unusual_average(numbers_list):
    average_list = []
    average_sum = 0
    for index in range(len(numbers_list)):
        if numbers_list[index] > 100:
            break
        else:
            if numbers_list[index] > 0:
                average_list.append(numbers_list[index])
    if len(average_list) == 0:
        result = 0
    else:
        for index in range(len(average_list)):
            average_sum = average_sum + average_list[index]
        result = average_sum / len(average_list)
    return round(result)


result = get_unusual_average([5, 10, 15, 120, 2, 88, 22])
print(result)
print(get_unusual_average([20, 100, 60]))
print(get_unusual_average([-66, -100, 800, 20, 60]))
print(get_unusual_average([6, 2, 4, -6, -8, 90]))