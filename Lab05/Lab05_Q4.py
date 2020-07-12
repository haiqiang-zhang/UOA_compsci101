"""
Lab 5:
"""

def main():
    print("[313, 636, 2042, 40, 447] - ", end = "")
    count_same_start_end = get_count_same_start_end([313, 636, 2042, 40, 447])
    print(count_same_start_end)
    print("[101, 4559, 241, 124, 9249] - ", end = "")
    print(get_count_same_start_end([101, 4559, 241, 124, 9249]))
    print("[101, 45594, 1241, 9, 929] - ", end = "")
    print(get_count_same_start_end([101, 45594, 1241, 9, 929]))

def get_count_same_start_end(numbers_list):
    count_value = 0
    for index in range(len(numbers_list)):
        cache_string = str(numbers_list[index])
        if cache_string[0] == cache_string[-1]:
            count_value = count_value+1
    return count_value

main()








