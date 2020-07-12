"""
Stage 2 functions of Assignment 2
"""

import random

def main():
    selection = 1
    while selection > 0:
        selection = get_choice()
        if selection == 1:
            test_display_current_player()
        elif selection == 2:
            test_get_next_player()
        elif selection == 3:
            test_get_random_starting_player_name()
        elif selection == 4:
            test_add_dice_roll()
        elif selection == 5:
            test_get_starting_score()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# FIVE STAGE 2 FUNCTIONS
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def display_current_player(current_player):
    print(current_player,"'s turn:",sep="")
    return()

def get_next_player(current_player, player_name):
    if current_player == "Computer":
        result = player_name
    else:
        result = "Computer"
    return result

def get_random_starting_player_name(player_name):
    random_number = random.randrange(1,3)
    if random_number == 1:
        result = player_name
    else:
        result = "Computer"
    return result

def add_dice_roll(current_score, current_player):
    dice = random.randrange(1,7)
    print(current_player,"'s dice roll: ",dice,sep="")
    reload_score = current_score+dice
    return reload_score

def get_starting_score():
    starting_score = random.randrange(12,17)
    return starting_score
#-----------------------------
# get_choice()
#-----------------------------
def get_choice():
    print()
    print(" ", "." * 35)
    print("  1. display_current_player()")
    print("  2. get_next_player()")
    print("  3. get_random_starting_player_name()")
    print("  4. add_dice_roll()")
    print("  5. get_starting_score()")
    print("  0. Exit")
    selection = int(input("     Enter selection: "))
    print(" ", "." * 35)
    print()
    return selection
#-----------------------------
# Test display_current_player()
#-----------------------------
def test_display_current_player():
    print("Expected output:")
    print("Lee's turn:")
    print("Joseph's turn:")
    print("Gwendoline's turn:")
    print()
    print("Your output:")
    display_current_player("Lee")
    display_current_player("Joseph")
    display_current_player("Gwendoline")
#-----------------------------
# Test get_other_player()
#-----------------------------
def test_get_next_player():
    print("Expected output:")
    print("Computer")
    print("Malia")
    print("Computer")
    print()
    print("Your output:")
    print(get_next_player("David", "David"))
    print(get_next_player("Computer", "Malia"))
    print(get_next_player("Jack", "Jack"))
#-----------------------------
# Test get_random_starting_player_name()
#-----------------------------
def test_get_random_starting_player_name():
    print("Expected output:")
    print("Four lines of output and each line prints either 'Asad' or 'Computer'")
    print()
    print("Your output:")
    print(get_random_starting_player_name("Asad"))
    print(get_random_starting_player_name("Asad"))
    print(get_random_starting_player_name("Asad"))
    print(get_random_starting_player_name("Asad"))
#-----------------------------
# Test add_dice_roll()
#-----------------------------
def test_add_dice_roll():
    print("Expected output:")
    print("Four sets of two lines of output each.  The dice roll \n  number is random between 1 and 6.")
    print("The second line of output in each set\n  is the dice roll number \n  added to 12, 15, 17 and 19 respectively")
    print()
    print("Your output:")
    print(add_dice_roll(12, "Miriam"))
    print(add_dice_roll(15, "Joe"))
    print(add_dice_roll(17, "Miriam"))
    print(add_dice_roll(19, "Joe"))
#-----------------------------
# Test get_starting_score()
#-----------------------------
def test_get_starting_score():
    print("Expected output:")
    print("Each line of output is a random number\n  between 12 and 16 both inclusive")
    print()
    print("Your output:")
    print(get_starting_score())
    print(get_starting_score())
    print(get_starting_score())
    print(get_starting_score())
    
test_get_starting_score()
#main()
