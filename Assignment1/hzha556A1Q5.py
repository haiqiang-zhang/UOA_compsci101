"""
Name: Haiqiang Zhang
Username: hzha556
ID number: 237994789
Description: Q5   A program which implements a dice game.

"""


import random
current_score = 0
print("*"*45)
print("REACH 100 IN THREE ROUNDS!   Initial total: 0")
print("*"*45)
"""
round1
"""
print()
print()
print("Round 1:")
dice1 = str(random.randrange(1,6))
dice2 = str(random.randrange(1,6))
dice3 = str(random.randrange(1,6))
dice4 = str(random.randrange(1,6))
dice5 = str(random.randrange(1,6))
dice_slice = dice1+dice2+dice3+dice4+dice5         
print("Your dice:",dice1,dice2,dice3,dice4,dice5)
round_ten = int(input("  Tens? "))
round_unit = int(input("  Units? "))
dice_value = dice_slice[round_ten-1]+dice_slice[round_unit-1]
print("Dice value:", dice_value)
current_score = int(dice_value)
print("Your current total:",current_score)
"""
round2
"""
print()
print()
print("Round 2:")
dice1 = str(random.randrange(1,6))
dice2 = str(random.randrange(1,6))
dice3 = str(random.randrange(1,6))
dice4 = str(random.randrange(1,6))
dice5 = str(random.randrange(1,6))
dice_slice = dice1+dice2+dice3+dice4+dice5           
print("Your dice:",dice1,dice2,dice3,dice4,dice5)
round_ten = int(input("  Tens? "))
round_unit = int(input("  Units? "))
dice_value = dice_slice[round_ten-1]+dice_slice[round_unit-1]
print("Dice value:", dice_value)
current_score = int(dice_value)+current_score
print("Your current total:",current_score)
"""
round3
"""
print()
print()
print("Round 3:")
dice1 = str(random.randrange(1,6))
dice2 = str(random.randrange(1,6))
dice3 = str(random.randrange(1,6))
dice4 = str(random.randrange(1,6))
dice5 = str(random.randrange(1,6))
dice_slice = dice1+dice2+dice3+dice4+dice5          
print("Your dice:",dice1,dice2,dice3,dice4,dice5)
round_ten = int(input("  Tens? "))
round_unit = int(input("  Units? "))
dice_value = dice_slice[round_ten-1]+dice_slice[round_unit-1]
print("Dice value:", dice_value)
current_score = int(dice_value)+current_score
print("Your current total:",current_score)


print()
print()
print("*"*29)
print("Your final score:",current_score)
print("You are", abs(current_score-100),"away from the goal")
print("*"*29)
