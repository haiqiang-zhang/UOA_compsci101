
import random

def main():
    username = "hzha556" #change this to your username
    player_name = "Haiqiang Zhang" #change this name
    option_new_game = 1
    option_see_stats = 2
    option_quit = 0

    number_of_games = 0
    won_by_user = 0
    won_by_computer = 0

    display_introduction('   ', username, player_name)
    selection = option_new_game

    while selection !=  option_quit:
        selection = get_main_menu_selection(" " * 5)

        if selection == option_new_game:
            number_of_games += 1
            winner_name = play_a_game(player_name)

            if winner_name == player_name:
                won_by_user += 1
            elif winner_name == "Computer":
                won_by_computer += 1

        elif selection == option_see_stats:
            display_statistics(player_name, number_of_games, won_by_user, won_by_computer)

    display_statistics(player_name, number_of_games, won_by_user, won_by_computer)
    print()
    print("Thank you for playing Ventuno " + player_name)
    print()
#--------------------------------------------------------------
#--------------------------------------------------------------
# DO NOT CHANGE THE CODE ABOVE THIS LINE EXCEPT FOR THE FIRST LINE
#--------------------------------------------------------------

#--------------------------------------------------------------
# FOUR STAGE 1 FUNCTIONS
#--------------------------------------------------------------
#--------------------------------------------------------------
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

#--------------------------------------------------------------
#--------------------------------------------------------------
# FIVE STAGE 2 FUNCTIONS
#--------------------------------------------------------------
#--------------------------------------------------------------
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

#--------------------------------------------------------------
#--------------------------------------------------------------
# FIVE STAGE 3 FUNCTIONS
#--------------------------------------------------------------
#--------------------------------------------------------------
def display_current_scores(indent, score_player, score_computer, player_stays, computer_stays, player_name):
    print()
    display_line_of_symbols(indent,"-",37)
    display_line_of_symbols(indent,"-",37)
    if player_stays == True:
        print(indent,player_name,"'s score: ",score_player," - ",player_name," stays",sep="")
    else:
        print(indent,player_name,"'s score: ",score_player,sep="")
    if computer_stays == True:
        print(indent,"Computer's score: ",score_computer," - Computer stays",sep="")
    else:
        print(indent,"Computer's score: ",score_computer,sep="")    
    display_line_of_symbols(indent,"-",37)
    display_line_of_symbols(indent,"-",37)
    print()
    return()

def game_is_over(score_player, score_computer, player_stays, computer_stays):
    if score_player>21 or score_computer>21:
        game_status = True
    elif player_stays==True and computer_stays==True:
        game_status = True
    else:
        game_status = False
    return game_status

def get_winner_name(score_player, score_computer, player_name):
    if score_player==score_computer:
        result = "draw"
    elif score_player>21:
        result = "Computer"
    elif score_computer>21:
        result = player_name
    elif score_player>score_computer:
        result = player_name
    elif score_player<score_computer:
        result = "Computer"
    return result
    

def display_game_result(indent, score_player, score_computer, game_winner, player_name):
    print()
    display_line_of_symbols(indent,"+",25)
    display_line_of_symbols(indent,"+",25)
    print(indent,player_name,"'s score: ",score_player,sep="")
    print(indent,"Computer's score: ",score_computer,sep="")
    if game_winner=="Computer":
        print(indent,"Computer has won.",sep="")
    elif game_winner==player_name:
        print(indent,player_name," has won.  Well done!",sep="")
    elif game_winner=="draw":
        print(indent,"Result is a draw.",sep="")
    display_line_of_symbols(indent,"+",25)
    display_line_of_symbols(indent,"+",25)
    return()

def display_statistics(player_name, total_number_of_games, games_won_by_user, games_won_by_computer):
    print()
    print("*"*32)
    print("*"*32)
    print("  Number of games played: ",total_number_of_games,sep="")
    print("  Games won by ",player_name,": ",games_won_by_user,sep="")
    print("  Games won by Computer: ",games_won_by_computer,sep="")
    print("  Games resulting in a draw: ",total_number_of_games-games_won_by_user-games_won_by_computer,sep="")
    print()
    if games_won_by_user>games_won_by_computer:
        print("*** ",player_name," is winning by ",games_won_by_user-games_won_by_computer," *** ",sep="")
    elif games_won_by_user<games_won_by_computer:
        print("*** Computer is winning by ",games_won_by_computer-games_won_by_user," *** ",sep="")
    else:
        print("*** Final result is a draw ***")
    print("*"*32)
    print("*"*32)
    return()
#--------------------------------------------------------------
#--------------------------------------------------------------
# ONE STAGE 4 FUNCTION
#--------------------------------------------------------------
#--------------------------------------------------------------
def get_computer_selection(score_player, score_computer, player_stays):
    roll = 1
    stay = 2
    ventuno = 21
    if score_player>score_computer:
        computer_choice = roll
    elif player_stays==True and score_player<score_computer:
        computer_choice = stay
    elif score_player==score_computer and score_computer>=ventuno-5:
        if player_stays==True:
            computer_choice = stay
        else:
            computer_choice = roll
    elif score_player==score_computer and score_computer<ventuno-5:
            computer_choice = roll
    else:
        if score_computer>=ventuno-5:
            computer_choice = stay
        else:
            computer_choice = roll
    return computer_choice

#--------------------------------------------------------------
#--------------------------------------------------------------
# DO NOT CHANGE THE CODE BELOW THIS LINE
#--------------------------------------------------------------
#--------------------------------------------------------------
def play_a_game(player_name):
    ventuno = 21

    player_stays = False
    computer_stays = False

    roll = 1
    stay = 2

    score_player = get_starting_score()
    score_computer = get_starting_score()

    current_player = get_random_starting_player_name(player_name)
    display_current_scores(" " * 5, score_player, score_computer, player_stays, computer_stays, player_name)

    while not game_is_over(score_player, score_computer, player_stays, computer_stays):
        if current_player == "Computer":
            if not computer_stays:
                display_current_player(" " + current_player)
                selection = get_computer_selection(score_player, score_computer, player_stays)

                if selection == roll:
                    score_computer = add_dice_roll(score_computer, "  Computer")
                    if score_computer == ventuno:
                        computer_stays = True
                else:
                    computer_stays = True
        elif not player_stays:
            display_current_player(" " + current_player)
            selection = get_play_menu_selection(' ' * 3)
            print()
            if selection == roll:
                score_player = add_dice_roll(score_player, " " + player_name)
                if score_player == ventuno or (computer_stays and score_player > score_computer):
                    player_stays = True
            elif selection == stay:
                player_stays = True

        display_current_scores(" " * 5, score_player, score_computer, player_stays, computer_stays, player_name)
        current_player = get_next_player(current_player, player_name)


    game_winner = get_winner_name(score_player, score_computer, player_name)
    display_game_result("  ", score_player, score_computer, game_winner, player_name)
    return game_winner

main()
