""" Assignment 3 function 7"""

def main():
    print_header(7, "is_a_valid_date()")
    print("1.", is_a_valid_date("January 21"))
    print("2.", is_a_valid_date("Auust 3"))
    print("3.", is_a_valid_date(" June   15B "))
    print("4.", is_a_valid_date("February 0"))
    print("5.", is_a_valid_date(" December 3K1"))
    print("6.", is_a_valid_date("January 28 6"))
    print("7.", is_a_valid_date(" January 6  "))
    print("8.", is_a_valid_date(" January   "))
#--------------------------------------------------
# 7777777777777777777777777777777777777777777777777
# Returns True if the parameter string is a
# valid date, otherwise returns False
#--------------------------------------------------
def is_a_valid_date(date_str):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    list_date = date_str.split()
    if list_date[0] in month_names:
        most_day = days_in_month[month_names.index(list_date[0])]
        if len(list_date) == 2 and list_date[1].isdigit():
            input_day = int(list_date[1])
            if input_day <= most_day and input_day > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
    
#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
