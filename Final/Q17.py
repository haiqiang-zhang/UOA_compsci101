def nested_loop_question(number):
    total = 0
    for i in range(1, number + 1):
        for j in range(i):
            total += 1
    return total




# input_number = 0
# while True:
#     if nested_loop_question(input_number) == 28:
#         print(nested_loop_question(input_number), input_number)
#     if nested_loop_question(input_number) == 0:
#         print(nested_loop_question(input_number), input_number)
#     if nested_loop_question(input_number) == 55:
#         print(nested_loop_question(input_number), input_number)
#     if nested_loop_question(input_number) == 91:
#         print(nested_loop_question(input_number), input_number)
#     input_number += 1

print(nested_loop_question(7))
print(nested_loop_question(0))
print(nested_loop_question(10))
print(nested_loop_question(13))