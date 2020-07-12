def main():
    word_list = ['hard', 'substitute', 'is', 'for', 'work', 'There', 'NO']
    print(get_o_words_count(word_list))

def get_o_words_count(word_list):
    count = 0
    for index in range(len(word_list)):
        string_word = str(word_list[index])
        if "o" in string_word or "O" in string_word:
            count = count+1
    return count
            
main()
