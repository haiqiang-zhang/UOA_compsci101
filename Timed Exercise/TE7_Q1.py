def get_biggest_two(numbers_tuple):
    if len(numbers_tuple) >= 2:
        numbers_list = list(numbers_tuple)
        numbers_list.sort()
        return (numbers_list[-2], numbers_list[-1])
    else:
        return numbers_tuple
numbers = (4, 7,   8,  1,   2,   5)
print(get_biggest_two(numbers))
print(get_biggest_two((23,)) )
print(get_biggest_two((81, 24, 11, 63, 70, 60, 26, 73, 14)) )