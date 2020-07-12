# def print_pyramid(number):
#     number_of_top_symbol = (number-1)*2 + 3
#     print("+"*number_of_top_symbol)
#     for y in range(number):
#         print("+"*int((number_of_top_symbol+1)/2-(y+1)), " "*(1+y*2), "+"*int((number_of_top_symbol+1)/2-(y+1)), sep="")
#     print("+" * number_of_top_symbol)
#     return

def print_pyramid(number):
    number_of_top_symbol = (number - 1) * 2 + 3
    print("+"*number_of_top_symbol)
    for y in range(number):
        space_number = 1+(y*2)
        symbol_number = int((number_of_top_symbol-space_number)/2)
        print("+"*symbol_number, " "*space_number, "+"*symbol_number, sep="")
    print("+" * number_of_top_symbol)
    return

print_pyramid(4)
print_pyramid(1)