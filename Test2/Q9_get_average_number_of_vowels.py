def get_average_number_of_vowels(words_list):
    if len(words_list) != 0:
        vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        count_vowels = 0
        for index in range(len(words_list)):
            for str_index in range(len(words_list[index])):
                if words_list[index][str_index] in vowels_list:
                    count_vowels += 1
        result = round(count_vowels/len(words_list), 1)
    else:
        result = 0
    return result








words = ["Beautiful", "Queen", "scratched", "Queueing"]
print(get_average_number_of_vowels(words))
print(get_average_number_of_vowels([]))