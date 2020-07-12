"""
Name: Haiqiang Zhang
Username: hzha556
ID number: 237994789
Description: Q4   A program which solves the change-making problem for a particular currency.
"""
num = int(input("Value: "))
hundred = num // 100
fifty = (num % 100) // 50
twenty_five = (num % 50) // 25
ten = (num % 25) // 10
five = (num - hundred*100 - fifty*50 - twenty_five*25 - ten*10)//5
one = num % 5
print()
print("You will need:")
print("="*19)
print("  100s:",hundred)
print("   50s:",fifty)
print("   25s:",twenty_five)
print("   10s:",ten)
print("    5s:",five)
print("    1s:",one)
print("="*19)
