"""
Lab 6:

"""

def main():
    word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
    print(word_list)
    shortest_length = get_shortest_length(word_list)
    print(shortest_length)
    print()

    word_list = ['cat', 'the', 'a', 'bag', 'let', 'out', 'can']
    print(word_list)
    print(get_shortest_length(word_list))
    print()

    word_list = ['it', 'the', 'the', 'the', 'out', 'big', 'I']
    print(word_list)
    print(get_shortest_length(word_list))

def get_shortest_length(word_list):
    if len(word_list)!= 0:
        length = len(word_list[0])
        for index in range(1, len(word_list)):
            if len(word_list[index]) < length:
                length = len(word_list[index])
    else:
        length = 0

    return length



main()








