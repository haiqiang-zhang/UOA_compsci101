def get_string_without_matches(letters_to_check, letters):
    new_string = str()
    for index in range(len(letters_to_check)):
        if letters[index] == letters_to_check[index]:
            new_string += " "
        else:
            new_string += letters_to_check[index]
    return new_string







print("***" + get_string_without_matches("CADB", "CDDB") + "***")
print("***" + get_string_without_matches("AADD", "CCCA") + "***")
print("***" + get_string_without_matches("CBBA", "CCCA") + "***")