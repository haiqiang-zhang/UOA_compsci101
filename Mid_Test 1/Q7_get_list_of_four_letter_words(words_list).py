def get_list_of_four_letter_words(words_list):
    result = []
    for index in range(len(words_list)):
        if len(words_list[index]) == 4:
            result.append(words_list[index].lower())
    return result




words = get_list_of_four_letter_words(['into', 'elephant', 'room', 'the'])
print(words)
print(get_list_of_four_letter_words(['hole', 'down', 'the', 'goes', 'rabbit']))
print(get_list_of_four_letter_words(['WATER', 'POND', 'OUT', 'FISH']))
print(get_list_of_four_letter_words([]))