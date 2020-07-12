prompt = input("Enter a word: ")
first_char = prompt[0]
last_char = prompt[len(prompt)-1]
print("The new word is ",last_char,prompt[1:len(prompt)-1],first_char,sep="")
