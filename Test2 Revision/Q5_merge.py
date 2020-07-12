def  merge(dict1, dict2):
    for key in dict2:
        if key in dict1:
            for index in range(len(dict2[key])):
                if dict2[key][index] not in dict1[key]:
                    dict1[key].append(dict2[key][index])
                    dict1[key].sort()
    return



dict1 = {"A": [1, 2, 3, 5], "B": [1, 2, 8], "X": [0, 9], "N": [8]}
dict2 = {"A": [5], "B": [2, 4, 7], "T": [5, 6], "N": [3, 8]}
merge(dict1, dict2)
for k in sorted(dict1.keys()):
    print(k, ':', dict1[k])