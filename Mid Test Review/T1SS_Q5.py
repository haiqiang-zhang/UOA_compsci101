'''
Write a function in_range(n, outside_mode) that takes an integer n and a boolean outside_mode as parameters. The function returns True if n is in the range 1..10 (inclusive) and outside_mode is False. If outside_mode is True, the function returns True if the number is less than 1 or greater than 10.
In summary:
If outside_mode is False, returns True if n is within the range 1 - 10 (inclusive).
If outside_mode is True, returns True if n is outside the range 1 - 10 (i.e. less than 1 or greater than 10).
In all other cases returns False.
'''

def in_range(n, outside_mode):
    if n >= 1 and n <= 10 and outside_mode == False:
        return True
    elif (n < 1 or n > 10) and outside_mode == True:
        return  True
    else:
        return  False


print(in_range(5, False))
print(in_range(0, False))
print(in_range(1, False))
print(in_range(5, True))
print(in_range(1, True))
print(in_range(11, True))