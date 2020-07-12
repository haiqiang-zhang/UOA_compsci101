"""
Draws an ox pattern
Date-written: Semester One, 2020.
Author:
"""

def main():
    print_ox_xo_pattern(2, 3)
    print()
    
def print_ox_xo_pattern(number_of_rows, number_of_columns):
    for y in range(number_of_rows):
        if y%2 == 0:
            print_word_judgement = True
            for x in range(number_of_columns):
                if print_word_judgement == True:
                    print("o", end="")
                else:
                    print("x", end="")
                print_word_judgement = not print_word_judgement
        else:
            print_word_judgement = False
            for x in range(number_of_columns):
                if print_word_judgement == True:
                    print("o", end="")
                else:
                    print("x", end="")
                print_word_judgement = not print_word_judgement
        if y != number_of_rows-1:
            print()
    return()




main()
    

    
            
    
		
    
    
