"""
Draws a mirrored right-angle triangle pattern
Date-written: Semester 1, 2020.
Author:
"""

def main():
    print_mirrored_right_angle_triangle(5, '*')
    print_mirrored_right_angle_triangle(5, 3)
    
def print_mirrored_right_angle_triangle(number_of_rows, style):
    if str(style).isdigit() == True:
        for y in range(number_of_rows):
            print(" "*(number_of_rows-(y+1)), end="")
            for x in range(style, style+y+1):
                print(x, sep="", end="")
            if y != number_of_rows-1:
                print()
    else:
        for y in range(1, number_of_rows+1):
            print(" " * (number_of_rows-y), style * y, sep="")
    return ()





main()
