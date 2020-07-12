def booleans_1(number1, number2):
    if len(str(number1)) == 3 and (number1 % number2 == 0 or number2 % number1 == 0):
        print("Yes")

def booleans_2(word1, word2, letter):
    if word1[0] == word2[0] and letter in word1 and letter in word2:
        print("Yes")

def booleans_3(value):
    if value > 14 and value < 65 and value % 5 == 0 or value % 2 == 0:
        print("A")
    elif value % 3 == 0 or value % 2 == 0 and value > 42:
        print("B")
    elif value < 54:
        print("C")
    else:
        print("D")

def main():
    booleans_3(20)
    booleans_3(81)
    booleans_3(11)
    booleans_3(101)

# booleans_1(200,200)
# booleans_2("abc","ac","b")


main()