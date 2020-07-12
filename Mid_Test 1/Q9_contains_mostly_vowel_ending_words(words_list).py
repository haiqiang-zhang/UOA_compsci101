def contains_mostly_vowel_ending_words(words_list):
    vowels = "aeiouAEIOU"
    result = bool()
    for index in range(len(words_list)):
        if len(words_list[index]) > 2:
            if words_list[index][-1] in vowels:
                result = True
            else:
                result = False
                break
        else:
            result = True
    return result

print(contains_mostly_vowel_ending_words(['file', 'barrel', 'like', 'shoo', 'sh', 'pi']))
print(contains_mostly_vowel_ending_words(['file', 'barre', 'like', 'shoo', 'so', 'pi']))
print(contains_mostly_vowel_ending_words(['do', 'he', 'in', 'go', 'to', 'it']))
print(contains_mostly_vowel_ending_words([]))