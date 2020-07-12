def function1(num_list1, num_list2):
    '''
    >>> function1([1,2],[1,2,3])
    Error, parameters incompatible!
    >>> function1([1,1,2],[1,1,1])
    num_list1.num_list2 = 4
    <BLANKLINE>
    ||num_list1 - num_list2|| = 1.0
    >>> function1([77,77,77],[20,12,11])
    num_list1.num_list2 = 3311
    <BLANKLINE>
    ||num_list1 - num_list2|| = 108.77
    >>> function1([1,12,111], [12,111,2222])
    num_list1.num_list2 = 247986
    <BLANKLINE>
    ||num_list1 - num_list2|| = 213.35
    '''
    if len(num_list1) != len(num_list2):
        print("Error, parameters incompatible!")
    else:
        calculation1 = 0
        for i in range(len(num_list1)):
            calculation1 += num_list1[i] * num_list2[i]
        calculation2 = 0
        for i in range(len(num_list1)):
            calculation2 += (num_list1[i] - num_list2[i]) ** 2
        calculation2 = round(calculation2 ** 0.5, 2)
        print("num_list1.num_list2 =", calculation1)
        print()
        print("||num_list1 - num_list2|| =", calculation2)

import doctest
doctest.testmod()


