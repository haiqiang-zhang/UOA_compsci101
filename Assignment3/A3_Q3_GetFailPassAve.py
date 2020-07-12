""" Assignment 3 function 3"""

def main():
    print_header(3, "get_fail_pass_average()")
    print("1.", get_fail_pass_average([63, 65, 33]))
    print("2.", get_fail_pass_average([63, 62, 100, 100]))
    print("3.", get_fail_pass_average([33, 42, 20, 10]))
    print("4.", get_fail_pass_average([50, 50, 100, 0]))

#--------------------------------------------------
# 3333333333333333333333333333333333333333333333333
# Returns a Python list containing the average fail
# mark and the average pass mark.
#--------------------------------------------------
def get_fail_pass_average(a_list):
    moreFifty = []
    lessFifty = []
    sum_more = 0
    sum_less = 0
    result = []
    for index in range(len(a_list)):
        if a_list[index] >= 50:
            moreFifty.append(a_list[index])
        else:
            lessFifty.append(a_list[index])
    if len(lessFifty) != 0:
        for index in range(len(lessFifty)):
            sum_less = lessFifty[index]+sum_less
        result.append(round(sum_less/len(lessFifty)))
    else:
        result.append(-1)    
    if len(moreFifty) != 0:
        for index in range(len(moreFifty)):
            sum_more = moreFifty[index]+sum_more
        result.append(round(sum_more/len(moreFifty)))
    else:
        result.append(-1)
    return result       

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
