def print_pattern(number):
    for index in range(number, 0, -1):
        print(" "*(number-index), str(index)*index, sep="")
    return()



print_pattern(6)
print_pattern(4)