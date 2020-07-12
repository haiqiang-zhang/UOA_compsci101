def print_board(board):
    for row in board:
        print(row)


def player_turn(board, position, symbol):
    index = 0
    invacent_index = []
    while index <= len(board)-1:
        str_index = 0
        while str_index <= len(board[index])-1:
            if board[index][str_index] == "0" or board[index][str_index] == "X":
                invacent_index.append(index*3+str_index+1)
            str_index += 1
        index += 1
    if position in invacent_index:
        print("Invalid move, try again.")
    else:
        for index in range(len(board)):
            for str_index in range(len(board[index])):
                if position == index*3+str_index+1:
                    board_str_list = list(board[index])
                    board_str_list[position-index*3-1] = symbol
                    board_str_list = "".join(board_str_list)
                    board.pop(index)
                    board.insert(index, board_str_list)
    return













board = ["###", "###", "###"]
print("Start")
print()
print_board(board)
print("\nTurn 1")
player_turn(board, 5, "X")
print()
print_board(board)


board = ["###","###","###"]
print("Start")
print()
print_board(board)
print("\nTurn 1")
player_turn(board,5,"X")
print()
print_board(board)
print("\nTurn 2")
player_turn(board,5,"0")
print()
print_board(board)