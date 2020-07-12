"""
Lab 6:

"""

def main():
    word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
    word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
    print(word_list)
    insert_word(word_list, "water", "bank")
    print(word_list)
    print()

    word_list = ['cat', 'the', 'bag', 'let', 'out', 'can']
    print(word_list)
    insert_word(word_list, "dog", "let")
    print(word_list)
    print()

    word_list = ['it', 'the', 'out', 'big', 'if']
    print(word_list)
    insert_word(word_list, "large", "bag")
    print(word_list)

def insert_word(word_list, word_to_insert, before_this_word):
    if before_this_word in word_list and word_to_insert not in word_list:
        insert_index = word_list.index(before_this_word)
        word_list.insert(insert_index, word_to_insert)
    return()

main()








