def print_hollow_square(symbols, number_of_rows):
    '''
    >>> print_hollow_square('#', 8)
    ########
    #      #
    #      #
    #      #
    #      #
    #      #
    #      #
    ########
    >>> print_hollow_square("$", 3)
    $$$
    $ $1
    $$$
    '''
    print(symbols*number_of_rows)
    for y in range(number_of_rows-2):
        for x in range(number_of_rows):
            if x == 0 or x == number_of_rows-1:
                print(symbols, end="")
            else:
                print(" ", end="")
        print()
    print(symbols*number_of_rows)
    return


print_hollow_square('#', 8)
print_hollow_square("$", 3)

import doctest
doctest.testmod()