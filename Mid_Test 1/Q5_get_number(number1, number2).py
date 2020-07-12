def get_number(number1, number2):
    result = str(number1)[0] + str(number2)[-1]
    return int(result)



print(get_number(76325, 321))
print(get_number(3, 2))
print(get_number(50004, 2))
print(get_number(0, 0))