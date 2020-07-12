"""
Lab 6:

"""

def main():
    numbers_list = [31, 636, 2042, 40, 447]
    print(numbers_list)
    increase_decrease(numbers_list)
    print(numbers_list)
    print()

    numbers_list = [11, 4559, 241, 99, 100]
    print(numbers_list)
    increase_decrease(numbers_list)
    print(numbers_list)
    print()

    numbers_list = [101, 45594, 1241, 9, 92]
    print(numbers_list)
    increase_decrease(numbers_list)
    print(numbers_list)

def increase_decrease(numbers_list):
    prompt = 0
    for index in range(len(numbers_list)):
        if numbers_list[index] < 100:
            prompt = numbers_list[index] * 10
            numbers_list.pop(index)
            numbers_list.insert(index, prompt)
        else:
            prompt = numbers_list[index] // 10
            numbers_list.pop(index)
            numbers_list.insert(index, prompt)
    return ()


main()








