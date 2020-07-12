def main():
    a_dict = create_dict([567, 3451, 11, 97, 83])
    print(a_dict)
    print_dict_in_key_order(a_dict)

def create_dict(a_list):
    a_dict = {}
    for num in a_list:
        a_key = num % 10
        if a_key in a_dict:
            if num not in a_dict[a_key]:
                a_dict[a_key].append(num)
                a_dict[a_key].sort()
        else:
            a_dict[a_key] = [num]
    return a_dict



def print_dict_in_key_order(a_dict):
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        print(key, ":", a_dict[key])

main()
