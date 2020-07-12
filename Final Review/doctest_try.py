def swap_halves(numbers):
    '''
    >>> swap_halves('10')
    '01'
    >>> swap_halves('100')
    '100'
    '''
    mid = len(numbers)//2
    return numbers[mid:] + numbers[0:mid]



import doctest
doctest.testmod()