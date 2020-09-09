phrase = "Nobody   is    perfect"
phrase = phrase.lower()
list_phrase = phrase.split()
reconstruct_phrase = ""
for index in range(len(list_phrase)):
    reconstruct_phrase += list_phrase[index][0] + "_"*(len(list_phrase[index])-2) + list_phrase[index][-1]
    if index != len(list_phrase) - 1:
        reconstruct_phrase += "  "

print("*"*(len(reconstruct_phrase)+6))
print("** ",end="")
print(reconstruct_phrase, end="")
print(" **")
print("*"*(len(reconstruct_phrase)+6))
