def get_string_without_matches(letters_to_check, letters):
    new_string = str()
    for index in range(len(letters_to_check)):
        if letters_to_check[index] == letters[index]:
            new_string += " "
        else:
            new_string += letters_to_check[index]
    return new_string




def get_number_correct_not_in_place(hidden_letters, user_letters):
    new_string = get_string_without_matches(hidden_letters, user_letters)
    index1 = 0
    while index1 < len(new_string):
        if new_string[index1] not in user_letters:
            new_string = new_string[:index1] + new_string[index1+1:]
        else:
            index1 += 1
    index2 = 0

    while index2 < len(new_string):
        if new_string[index2] in new_string[:index2] or new_string[index2] in new_string[index2+1:]:
            new_string = new_string[:index2] + new_string[index2 + 1:]
        else:
            index2 += 1
    return len(new_string)












print(get_number_correct_not_in_place("CACC", "CACC"))

print(get_number_correct_not_in_place("AACC", "CAAA"))

print(get_number_correct_not_in_place("BABC", "BBDB"))

print(get_number_correct_not_in_place("DDBA", "DDDA"))