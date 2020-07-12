'''
Write a Python program which does the following:
* prompts the user to enter a word
* prints a new word made up of the same letters as the word entered by the user but with every second letter replaced by a hyphen.
'''
prompt = input("Enter a word: ")
result = str()
for index in range(len(prompt)):
    if index%2 == 0:
        result = result + prompt[index]
    else:
        result = result + "-"
print(result)


