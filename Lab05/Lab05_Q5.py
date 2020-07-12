"""
Lab 5:
"""

def main():
    print_longest_word(['fish', 'barrel', 'like', 'shooting', 'in', 'a'])
    print_longest_word(['cat', 'the', 'the', 'bag', 'let', 'out', 'of'])
    print_longest_word(['the', 'the', 'bag', 'let', 'out', 'of', 'cat'])

def print_longest_word(word_list):
    longest_word = str(word_list[0])
    for index in range(1,len(word_list)):
        if len(str(word_list[index])) >= len(longest_word):
            longest_word = str(word_list[index])
    print(longest_word)
    return()
            
        

main()








