def print_right_angle_traingles(symbol1, symbol2, number_of_rows):
    for y in range(number_of_rows-1):
        for x in range(number_of_rows-y-1):
            print(symbol1,end="")
        for x in range(y+1):
            print(symbol2,end="")
        print()
    return()



print_right_angle_traingles('*', '-', 5)
print_right_angle_traingles("$",'-', 3)