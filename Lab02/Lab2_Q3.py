prompt = input("Enter your name in the format first-name middle-name family-name: ")
number_family = prompt.rfind(" ") +1
family = prompt[number_family:len(prompt)]
middle = prompt[prompt.find(" ")+1:prompt.rfind(" ")]
first = prompt[0:prompt.find(" ")]
print("Your new name is",family,middle,first)
