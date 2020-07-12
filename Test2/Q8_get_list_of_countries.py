def get_list_of_countries(filename):
    input_file = open(filename, "r")
    file_list = input_file.read().split()
    return file_list

def create_country_code_dictionary(lines_list):
    result_dictionary = {}
    for index in range(len(lines_list)):
        colon_index = lines_list[index].find(":")
        result_dictionary[lines_list[index][:colon_index]] = lines_list[index][colon_index+1:]
    return result_dictionary









lines = get_list_of_countries('countries.txt')
countries_dictionary = create_country_code_dictionary(lines)
for key in sorted(countries_dictionary.keys()):
    print(key, countries_dictionary[key])