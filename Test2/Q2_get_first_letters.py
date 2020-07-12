def get_first_letters(word1, word2, word3):
    result = word1[0].upper() + word2[0].upper() + word3[0].upper()
    return result



print(get_first_letters("be", "back", "soon"))
print(get_first_letters("before", "anyone", "else"))
print(get_first_letters("random", "Access", "memory"))