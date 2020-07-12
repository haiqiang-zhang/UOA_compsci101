def get_inner_number(number):
    result = str(abs(number))
    if len(result) >= 3:
        result = int(result[1:len(result)-1])
    else:
        result = int(0)
    return result

print(get_inner_number(8))    
