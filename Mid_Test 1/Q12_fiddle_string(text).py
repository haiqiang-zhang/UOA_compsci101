def fiddle_string(text):
    if len(text)%2 != 0:
        if len(text) == 1:
            result = text
        else:
            index_odd = int((len(text)-1)/2)
            result = text[index_odd+1:]+text[index_odd]+text[:index_odd]
    else:
        index_even = int(len(text)/2)
        result = text[index_even:]+text[:index_even]
    return result


word = "Damir"
print("Original word:",word,"\nNew word:",fiddle_string(word))
word = "barbeque"
print("Original word:",word,"\nNew word:",fiddle_string(word))


print(fiddle_string("oi"))