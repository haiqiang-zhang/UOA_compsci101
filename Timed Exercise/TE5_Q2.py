def get_shortened_words(word_list):
    shortened_list = []
    for index in range(len(word_list)):
        if len(word_list[index]) > 2:
            shortened_list.append((word_list[index])[0]+(word_list[index])[-1])
    return shortened_list


word_list = ['you', 'it', 'do', 'do', 'whatever', 'well']
short_words = get_shortened_words(word_list)
print(short_words)
print(get_shortened_words(['fish', 'out', 'of', 'water']))
print(get_shortened_words(['am', 'as', 'a', 'go']))
