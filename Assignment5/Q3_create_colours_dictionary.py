def create_colours_dict(lines):
    result_dict = {}
    for index in range(len(lines)):
        left_key = int(lines[index][:1])
        right_value = lines[index][2:]
        result_dict[left_key] = right_value
    return result_dict






lines = ['1:brown', '2:bisque', '3:white', '4:purple', '5:tan']
cd = create_colours_dict(lines)
for k in sorted(cd.keys()):
    print(k, cd[k])
lines = ['1:grey', '2:black', '3:dimgray']
cd = create_colours_dict(lines)
for k in sorted(cd.keys()):
    print(k, cd[k])