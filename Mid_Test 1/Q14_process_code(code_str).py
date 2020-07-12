# def process_code(code_str):
#     result = 0
#     if int(code_str[0]) == len(code_str)-1:
#         result = int(code_str[1:])
#     elif len(code_str) >= 4 and len(code_str) < 6:
#         for index_first in range(len(code_str)-1):
#             for index_second in range(index_first + 2, len(code_str)-1):
#                 if int(code_str[index_first]) == index_second - index_first - 1 and int(code_str[index_second]) == len(code_str) - 1 - index_second:
#                     result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:])
#                     return result
#     elif len(code_str) >= 6 and len(code_str) < 8:
#         for index_first in range(len(code_str) - 1):
#             for index_second in range(index_first + 2, len(code_str) - 1):
#                 for index_third in range(index_second + 2, len(code_str)+10):
#                     if index_third < len(code_str) - 1:
#                         if int(code_str[index_third]) == len(code_str) - 1 - index_third and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                             result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:])
#                             return result
#                     if int(code_str[index_first]) == index_second - index_first - 1 and int(code_str[index_second]) == len(code_str) - 1 - index_second:
#                         result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:])
#                         return result
#     elif len(code_str) >= 8 and len(code_str) < 10:
#         for index_first in range(len(code_str) - 1):
#             for index_second in range(index_first + 2, len(code_str) - 1):
#                 for index_third in range(index_second + 2, len(code_str)+10):
#                     for index_fourth in range(index_third + 2, len(code_str)+10):
#                         if index_fourth < len(code_str) - 1 and index_third < len(code_str) - 1:
#                             if int(code_str[index_fourth]) == len(code_str)-1 - index_fourth and int(code_str[index_third]) == index_fourth - index_third -1 and int(code_str[index_second]) == index_third - index_second -1 and int(code_str[index_first]) == index_second - index_first -1:
#                                 result = int(code_str[index_first+1:index_second]) + int(code_str[index_second+1:index_third]) + int(code_str[index_third+1:index_fourth]) + int(code_str[index_fourth+1:])
#                                 return result
#                         if index_third < len(code_str) - 1:
#                             if int(code_str[index_third]) == len(code_str) - 1 - index_third and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                                 result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:])
#                                 return result
#                         if int(code_str[index_first]) == index_second - index_first - 1 and int(code_str[index_second]) == len(code_str) - 1 - index_second:
#                             result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:])
#                             return result
#     elif len(code_str) >= 10 and len(code_str) < 12:
#         for index_first in range(len(code_str) - 1):
#             for index_second in range(index_first + 2, len(code_str) - 1):
#                 for index_third in range(index_second + 2, len(code_str)+10):
#                     for index_fourth in range(index_third + 2, len(code_str)+10):
#                         for index_fifth in range(index_fourth + 2, len(code_str)+10):
#                             if index_fifth < len(code_str)-1 and index_fourth < len(code_str)-1 and index_third < len(code_str)-1:
#                                 if int(code_str[index_fifth]) == len(code_str)-1 - index_fifth and int(code_str[index_fourth]) == index_fifth - index_fourth -1 and int(code_str[index_third]) == index_fourth - index_third -1 and int(code_str[index_second]) == index_third - index_second -1 and int(code_str[index_first]) == index_second - index_first -1:
#                                     result = int(code_str[index_first+1:index_second]) + int(code_str[index_second+1:index_third]) + int(code_str[index_third+1:index_fourth]) + int(code_str[index_fourth+1:index_fifth]) + int(code_str[index_fifth+1:])
#                                     return result
#                             if index_fourth < len(code_str)-1 and index_third < len(code_str)-1:
#                                 if int(code_str[index_fourth]) == len(code_str) - 1 - index_fourth and int(code_str[index_third]) == index_fourth - index_third - 1 and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                                     result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:index_fourth]) + int(code_str[index_fourth + 1:])
#                                     return result
#                             if index_third < len(code_str)-1:
#                                 if int(code_str[index_third]) == len(code_str) - 1 - index_third and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                                     result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:])
#                                     return result
#                             elif int(code_str[index_first]) == index_second - index_first - 1 and int(code_str[index_second]) == len(code_str) - 1 - index_second:
#                                 result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:])
#                                 return result
#     elif len(code_str) >= 12:
#         for index_first in range(len(code_str) - 1):
#             for index_second in range(index_first + 2, len(code_str) - 1):
#                 for index_third in range(index_second + 2, len(code_str)+20):
#                     for index_fourth in range(index_third + 2, len(code_str)+20):
#                         for index_fifth in range(index_fourth + 2, len(code_str)+20):
#                             for index_sixth in range(index_fifth + 2, len(code_str)+20):
#                                 if index_sixth < len(code_str)-1 and index_fifth < len(code_str)-1 and index_fourth < len(code_str)-1 and index_third < len(code_str)-1:
#                                     if int(code_str[index_sixth]) == len(code_str) - 1 - index_sixth and int(code_str[index_fifth]) == len(code_str) - 1 - index_fifth and int(code_str[index_fourth]) == index_fifth - index_fourth - 1 and int(code_str[index_third]) == index_fourth - index_third - 1 and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                                         result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:index_fourth]) + int(code_str[index_fourth + 1:index_fifth]) + int(code_str[index_fifth + 1:index_sixth]) + int(code_str[index_sixth+1:])
#                                         return result
#                                 if index_fifth < len(code_str)-1 and index_fourth < len(code_str)-1 and index_third < len(code_str)-1:
#                                     if int(code_str[index_fifth]) == len(code_str)-1 - index_fifth and int(code_str[index_fourth]) == index_fifth - index_fourth -1 and int(code_str[index_third]) == index_fourth - index_third -1 and int(code_str[index_second]) == index_third - index_second -1 and int(code_str[index_first]) == index_second - index_first -1:
#                                         result = int(code_str[index_first+1:index_second]) + int(code_str[index_second+1:index_third]) + int(code_str[index_third+1:index_fourth]) + int(code_str[index_fourth+1:index_fifth]) + int(code_str[index_fifth+1:])
#                                         return result
#                                 if index_fourth < len(code_str)-1 and index_third < len(code_str)-1:
#                                     if int(code_str[index_fourth]) == len(code_str) - 1 - index_fourth and int(code_str[index_third]) == index_fourth - index_third - 1 and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                                         result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:index_fourth]) + int(code_str[index_fourth + 1:])
#                                         return result
#                                 if index_third < len(code_str)-1:
#                                     if int(code_str[index_third]) == len(code_str) - 1 - index_third and int(code_str[index_second]) == index_third - index_second - 1 and int(code_str[index_first]) == index_second - index_first - 1:
#                                         result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:index_third]) + int(code_str[index_third + 1:])
#                                         return result
#                                 elif int(code_str[index_first]) == index_second - index_first - 1 and int(code_str[index_second]) == len(code_str) - 1 - index_second:
#                                     result = int(code_str[index_first + 1:index_second]) + int(code_str[index_second + 1:])
#                                     return result
#
#
# def process_code(code_str):
#     index = -2
#     point_index = 0
#     sum = 0
#     right_code = code_str[index+1:]
#     while index >= -len(code_str):
#         print(right_code)
#         if point_index == 0:
#             if int(code_str[index]) == len(right_code):
#                 sum = sum + int(right_code)
#                 point_index = index
#                 index = index - 2
#                 right_code = code_str[index+1:point_index]
#             else:
#                 index = index - 1
#                 right_code = code_str[index + 1:]
#         else:
#             if int(code_str[index]) == len(right_code):
#                 sum = sum + int(right_code)
#                 point_index = index
#                 index = index - 2
#                 right_code = code_str[index + 1:point_index]
#             else:
#                 index = index -1
#                 right_code = code_str[index+1:point_index]
#     return sum

def process_code(code_str):
    index = 0
    sum = 0
    while index < len(code_str)-1:
        sum = int(code_str[index+1:int(code_str[index])+index+1]) + sum
        index = index + int(code_str[index])+1
    return sum


code = "123456"
print("Code:", code, "Result:", process_code(code))
code = "245590000"
print("Code:", code, "Result:", process_code(code))
print(process_code("12345623346666"))




