"""
Lab 7:

"""

def main():
    words = ('carry', 'stick', 'big', 'a', 'and', 'speak', 'softly')
    numbers = (23, 40, 19, 22, 42, 41, 63)
    print(get_two_words(numbers, words))
    print()

    words = ('whole', 'kit', 'the', 'and', 'caboodle')
    numbers = (76, 81, 62, 83, 87)
    print(get_two_words(numbers, words))
    print()

    words = ('mouth', 'in', 'look', 'do', 'gift', 'a', 'the', 'horse', 'not')
    numbers = (81, 24, 11, 63, 70, 60, 26, 73, 14)
    print(get_two_words(numbers, words))

def get_two_words(numbers_tuple, words_tuple):
    numbers_list = list(numbers_tuple)
    numbers_list.sort()
    index_first_number = numbers_tuple.index(numbers_list[0])
    index_second_number = numbers_tuple.index(numbers_list[1])
    return (words_tuple[index_first_number], words_tuple[index_second_number])




main()








