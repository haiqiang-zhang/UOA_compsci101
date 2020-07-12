"""
Stage 1 functions of Assignment 2
"""
import random

def main():
    selection = 1
    while selection > 0:
        selection = get_choice()
        if selection == 1:
            test_display_line_of_symbols()
        elif selection == 2:
            test_display_introduction()
        elif selection == 3:
            test_get_play_menu_selection()
        elif selection == 4:
            test_get_main_menu_selection()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# FOUR STAGE 1 FUNCTIONS
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def display_line_of_symbols(indent, symbol, how_many):
    line = indent + (symbol*how_many)
    print(line)
    return()

def display_introduction(indent, username, name):
    print()
    display_line_of_symbols(indent,'=',27)
    print(indent,"Ventuno written by ",username,sep="")
    print(indent,"Welcome ",name,sep="")
    display_line_of_symbols(indent,'=',27)
    print()
    return()

def get_play_menu_selection(indent):
    print()
    print(indent,"1. ROLL",sep="")
    print(indent,"2. STAY",sep="")
    input_prompt = indent + " "*3 + "Enter selection: "
    select = int(input(input_prompt))
    return select

def get_main_menu_selection(indent):
    print()
    print(indent,"1. PLAY A NEW GAME",sep="")
    print(indent,"2. SEE STATS",sep="")
    print(indent,"0. QUIT",sep="")
    input_prompt = indent + " "*3 + "Enter selection: "
    select = int(input(input_prompt))
    return select
#-----------------------------
# get_choice()
#-----------------------------
def get_choice():
    print()
    print(" ", "." * 35)
    print("  1. display_line_of_symbols()")
    print("  2. display_intro()")
    print("  3. get_play_menu_selection()")
    print("  4. get_main_menu_selection()")
    print("  0. Exit")
    selection = int(input("     Enter selection: "))
    print(" ", "." * 35)
    print()
    return selection
#-----------------------------
# Test display_line_of_symbols()
#-----------------------------
def test_display_line_of_symbols():
    print("Expected output:")
    print("===========================")
    print("     ++++++++++++")
    print("   ***************")
    print("        >>>>>>>>")
    print("Your output:")
    indent = ""
    display_line_of_symbols(indent, "=", 27)
    indent = "     "
    display_line_of_symbols(indent, "+", 12)
    indent = "   "
    display_line_of_symbols(indent, "*", 15)
    indent = "        "
    display_line_of_symbols(indent, ">", 8)
#-----------------------------
# Test display_intro()
#-----------------------------
def test_display_introduction():
    print("Expected output:")
    print()

    print("   ===========================")
    print("   Ventuno written by abcd001")
    print("   Welcome Bill")
    print("   ===========================")
    print()
    print()
    print("     ===========================")
    print("     Ventuno written by wxyz999")
    print("     Welcome Adeline")
    print("     ===========================")
    print()
    print("Your output:")
    display_introduction(' ' * 3, "abcd001", "Bill")
    display_introduction(' ' * 5, "wxyz999", "Adeline")
#-----------------------------
# Test get_play_menu_selection()
#-----------------------------
def test_get_play_menu_selection():
    print("Expected output if the user enters the number 2, then the number 1:")
    print()
    print("       1. ROLL")
    print("       2. STAY")
    print("          Enter selection: 2")
    print()
    print("    1. ROLL")
    print("    2. STAY")
    print("       Enter selection: 1")
    print(2, 1)
    print("Your output:")
    selection1 = get_play_menu_selection(' ' * 7)
    selection2 = get_play_menu_selection(' ' * 4)
    if selection1 != None and selection2 != None:
        print(selection1 * 1, selection2 * 1)
#-----------------------------
# Test get_main_menu_selection()
#-----------------------------
def test_get_main_menu_selection():
    print("Expected output if the user enters the number 2, then the number 3:")
    print()
    print("    1. PLAY A NEW GAME")
    print("    2. SEE STATS")
    print("    0. QUIT")
    print("       Enter selection: 2")
    print()
    print("       1. PLAY A NEW GAME")
    print("       2. SEE STATS")
    print("       0. QUIT")
    print("          Enter selection: 3")
    print(2, 3)
    print("Your output:")
    selection1 = get_main_menu_selection(' ' * 4)
    selection2 = get_main_menu_selection(' ' * 7)
    if selection1 != None and selection2 != None:
        print(selection1 * 1, selection2 * 1)


main()
