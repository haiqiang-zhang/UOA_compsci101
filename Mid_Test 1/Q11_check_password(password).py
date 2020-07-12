def check_password(password):
    digit_judge = bool()
    alpha_judge = bool()
    symbol_judge = bool()
    lenth_judge = bool()
    result = bool()
    symbol_list = [".",";","!","*","?"]
    for index in range(len(password)):
        if password[index].isdigit() == True:
            digit_judge = True
            break
    for index in range(len(password)):
        if password[index].isalpha() == True:
            alpha_judge = True
            break
    for index in range(len(password)):
        if password[index] in symbol_list:
            symbol_judge = True
            break
    if len(password) >= 8:
        lenth_judge = True
    if digit_judge and alpha_judge and symbol_judge and lenth_judge == True:
        result = True
    return result



password = "abc012"
print("Is",password,"valid:",check_password(password))
password = "abcd0123"
print("Is",password,"valid:",check_password(password))
password = "dAmIr007!"
print("Is",password,"valid:",check_password(password))





