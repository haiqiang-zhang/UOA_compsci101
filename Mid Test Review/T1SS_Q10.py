def main():
    process_sentence("z", "i saw zebras at the zoo today.")
    process_sentence("w", "i wonder why wayne hates wednesday.")
    process_sentence("a", "an angry armadillo went walking.")

def process_sentence(letter,sentence):
    index = 0
    space_index = []
    sentence_list = []
    while index < len(sentence):
        if sentence[index] == " ":
            space_index.append(index)
        index += 1
    index = 0
    sentence_list.append(sentence[:space_index[0]])
    while index < len(space_index):
        if index != len(space_index)-1:
            sentence_list.append(sentence[space_index[index]+1:space_index[index+1]])
        else:
            sentence_list.append(sentence[space_index[index]+1:])
        index += 1
    result = str()
    index = 0
    while index < len(sentence_list):
        if letter == sentence_list[index][0]:
            if sentence_list[index][-1] == ".":
                result = result + sentence_list[index][:-1] + "\n"
            else:
                result = result + sentence_list[index] + "\n"
        index += 1
    print(result)
    return()





main()