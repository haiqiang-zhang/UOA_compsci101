def convert_first_letter(names):
    for index in range(len(names)):
        first_letter_upper = names[index][0].upper()
        upper_names = first_letter_upper+names[index][1:]
        names.pop(index)
        names.insert(index, upper_names)
    return








names = ['karl', 'Orlando', 'carlo', 'zAC']
convert_first_letter(names)
print(names)
greeting = ['hello', 'well done', 'good morning']
convert_first_letter(greeting )
print(greeting)