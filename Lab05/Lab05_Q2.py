"""
Lab 5:
"""

def main():
    print_numbers(10, 25)
    print()
    print_numbers(25, 20)
    print()
    print_numbers(9, 33)
    print()

def print_numbers(number1, number2):
    for index in range(1,100):
        if index % number1 == 0 or index % number2 == 0:
            print(index, end=" ")
    return()

main()








