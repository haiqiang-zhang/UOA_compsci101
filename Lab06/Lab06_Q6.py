"""
Lab 6:

"""

def main():
    word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
    print(word_list)
    remove_short_words(word_list)
    print(word_list)
    print()

    word_list = ['cat', 'the', 'the', 'bag', 'let', 'out', 'can']
    print(word_list)
    remove_short_words(word_list)
    print(word_list)
    print()

    word_list = ['it', 'the', 'the', 'the', 'out', 'big', 'if']
    print(word_list)
    remove_short_words(word_list)
    print(word_list)

def get_shortest_length(word_list):
    if len(word_list) != 0:
        length = len(word_list[0])
        for index in range(1, len(word_list)):
            if len(word_list[index]) < length:
                length = len(word_list[index])
    else:
        length = 0
    return length


def remove_short_words(word_list):
    shortest_length = get_shortest_length(word_list)
    index = 0
    sync_index = 0
    while index <= sync_index:
        if len(word_list[index]) == shortest_length:
            word_list.pop(index)
        else:
            index += 1
        sync_index = len(word_list)-1
    return()



main()








