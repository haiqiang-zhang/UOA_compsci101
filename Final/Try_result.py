# nums = [18, 19, 20, 21, 22]
# nums[nums[3] - nums[0]] = 10
# print(nums)
# nums[nums[4] - nums[2]] = 10
# print(nums)
# nums[nums[4] - nums[0]] = 10
# print(nums)
# nums[nums[4] - nums[1]] = 10
# print(nums)
# nums[nums[2] - nums[2]] = 10
# print(nums)

# def secret(numbers):
#     for index in range(len(numbers)):
#         if numbers[index] == index:
#             return 0
#     return 1
# print(secret([2, 8, 0, 6, 8]))
# print(secret([9, 0, 0, 8, 4]))
# print(secret([1, 8, 6, 1, 8]))
# print(secret([2, 0, 7, 1, 9]))
# print(secret([3, 9, 7, 9, 5]))

def question(numbers):
    x = 0
    for index in range(5):
        if index < 2:
            x += numbers[index]
        elif index > 2:
            x -= numbers[index]
    return x
numbers = [2, 34, 40, 46, -10]
print(question(numbers))
numbers = [3, 48, 27, 37, 15]
print(question(numbers))
numbers = [39, 19, 43, 28, 27]
print(question(numbers))
numbers = [28, 29, 39, 47, 42]
print(question(numbers))
numbers = [23, 32, 6, 27, 5]
print(question(numbers))
