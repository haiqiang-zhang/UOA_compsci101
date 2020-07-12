str_input = input("Enter information: ")
str_list = str_input.split()
star_number = int(str_list[1]) - len(str_list[0])
print("*" * star_number, str_list[0] , sep="")