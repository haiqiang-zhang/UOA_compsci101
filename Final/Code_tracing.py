def main():
    result1 = function1(2, 5)
    print("A", result1)
    result2 = function1(8, 0)
    print("B", result2)
    result3 = function1(6, -1)
    print("C", result3)
    print(result1 + result2 + result3)

def function1(num1, num2):
    if num1 < num2 and num2 > 4:
        if num2 != 6:
            return num1 + num2
        else:
            return num1 - num2
    elif num2 < 0:
        return num1 * 2
    else:
        return num1 // 2

main()