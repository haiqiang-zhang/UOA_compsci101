'''
Write a program that keeps asking the user to enter integers until a negative integer is given. Your program will then output a message that indicates the sum of all the numbers entered but not including the negative number.

'''
sum = 0
while True:
    number = int(input("Enter a positive integer: "))
    if number >= 0:
        sum = sum + number
    else:
        print("The sum is ", sum, ".", sep="")
        break
