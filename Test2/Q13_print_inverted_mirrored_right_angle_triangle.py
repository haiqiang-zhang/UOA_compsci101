def print_inverted_mirrored_right_angle_triangle(symbols, index, number_of_rows):
    if index < len(symbols):
        for y in range(number_of_rows, 0, -1):
            print(" "*(number_of_rows-y), symbols[index]*y, sep="")
    else:
        for y in range(number_of_rows, 0, -1):
            print(" " * (number_of_rows - y),end="")
            for x in range(index, y+index):
                print(x, end="")
            print()
    return










print_inverted_mirrored_right_angle_triangle(['%', '$', '#', '@', '&', '*'], 2, 4)
print_inverted_mirrored_right_angle_triangle(['%', '$', '#'], 3, 5)

