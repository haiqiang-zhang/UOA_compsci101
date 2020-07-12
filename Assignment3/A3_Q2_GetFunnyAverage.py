""" Assignment 3 function 2"""

def main():
    print_header(2, "get_funny_average()")
    print("1.  [3, 12, 0, 25, 1] =>", get_funny_average([ 3, 12, 0, 25, 1]))
    print("2.  [-6, -32, 2, 0, -51, 1, 0, 0] =>", get_funny_average([-6, -32, 2, 0, -51, 1, 0, 0]))
    print("3.  [56, 0, 2, 0, 22] =>", get_funny_average([56, 0, 2, 0, 22]))
    print("4.  [56, 6, 0, -21, 0, 3, 4] =>", get_funny_average([-56, -3, 0, -21, 0, 6, 5]))
    print(get_funny_average([0,0,0]))
#--------------------------------------------------
# 22222222222222222222222222222222222222222222222222
# Returns the average of a list of numbers (excluding
# all zeroes and the minimum and maximum numbers)
#--------------------------------------------------
def get_funny_average(numbers):
    suma = 0
    nonzero_numbers = []
    numbers.sort()
    for index in range(len(numbers)):
        if numbers[index] != 0:
            nonzero_numbers.append(numbers[index])
    nonzero_numbers = nonzero_numbers[1:len(nonzero_numbers)-1]
    if len(nonzero_numbers) == 0:
        average = 0
    else:
        for index in range(len(nonzero_numbers)):
            suma = nonzero_numbers[index]+suma
        average = round(suma/len(nonzero_numbers))      
    return average
    
#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
