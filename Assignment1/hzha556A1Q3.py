"""
Name: Haiqiang Zhang
Username: hzha556
ID number: 237994789
Description: Q3   A program which decrypts a four-letter word.
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 6
prompt = input("Enter encrypted string: ")
one = alphabet[alphabet.find(prompt[0])-shift]
two = alphabet[alphabet.find(prompt[1])-shift]
three = alphabet[alphabet.find(prompt[2])-shift]
four = alphabet[alphabet.find(prompt[3])-shift]
print()
print("Unencrypted string: ",one,two,three,four,sep = "")
