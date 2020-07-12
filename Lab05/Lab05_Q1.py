"""
Lab 5:
"""

def main():
    print_even_numbers(2, 14)
    print_even_numbers(5, 16)
    print_even_numbers(65, 20)

def print_even_numbers(first_num, last_num):
    for index in range(first_num, last_num+1):
        if index % 2 == 0:
            print(index, end=" ")
    
    print()         

main()








