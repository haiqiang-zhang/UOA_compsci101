def get_ordered_words(word1, word2):
    if len(word1) > len(word2):
        result = word1 + " " + word2
    else:
        result = word2 + " " + word1
    return result


print(get_ordered_words("out", "dinner"))
print(get_ordered_words("dinner", "out"))
print(get_ordered_words("bb", "a"))