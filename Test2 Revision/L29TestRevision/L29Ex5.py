import math

def merge(dict1, dict2): 
    #complete this


def main():
    dict1 = {"A": [1, 2, 3, 5], "B": [1, 2, 8], "X": [0, 9], "N": [8]}
    dict2 = {"A": [5], "B": [2, 4, 7], "T": [5, 6], "N": [3, 8]}
    merge(dict1, dict2)
    for k in sorted(dict1.keys()):
        print(k, ':', dict1[k])


main()
