def judge_same_lens_and_character_set(value_one, value_two):
    if len(value_one) != len(value_two):
        return False
    for index in value_one:
        if index not in value_two:
            return False
    for index in value_two:
        if index not in value_one:
            return False
    return True


def get_count(list1, list2):
    '''
    Counting elements that are the same in positive order of list1 and reverse order of list2.
    '''
    count = 0
    min_length = min(len(list1), len(list2))
    for index1 in range(min_length):
        element1 = list1[index1]
        index2 = len(list2) - index1 - 1
        element2 = list2[index2]
        if element1 == element2:
            count = count + 1
        else:
            return count
    return count


print(get_count(["d","c", "b"],["a","b","c","d"]))