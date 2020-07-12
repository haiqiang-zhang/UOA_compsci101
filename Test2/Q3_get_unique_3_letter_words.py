def get_unique_3_letter_words(text):
    text_list = text.split()
    result = []
    for index in range(len(text_list)):
        if len(text_list[index]) == 3 and text_list[index].lower() not in result:
            result.append(text_list[index].lower())
    result.sort()
    return result









sentence = "In the Not Too distant future technology too may  not provide a solution to the problem"
words_list = get_unique_3_letter_words(sentence)
print(words_list)
words_list = get_unique_3_letter_words("I could agree with you but then we would both be wrong")
print(words_list)
words_list = get_unique_3_letter_words("I have nothing to declare except my genius")
print(words_list)