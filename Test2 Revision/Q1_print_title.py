def print_title(word):
    word = word.upper()
    for index in range(int((len(word)+1)/2)):
        print("-"*index, word[index:len(word)-index],sep="")
    return








print_title('marvellous')
print_title('fantastic')