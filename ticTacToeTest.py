import re

board = []
board_size = 3

def create_board(board_size):
    t = 1
    for i in range(1,board_size+1):
        line = []
        for j in range(1,board_size+1):
            line.append(str(t))
            t += 1
        board.append(line)


def modify_board(number, player):
    player_str = str(player).upper()
    number_str = str(number)
    for key_board, value_board in enumerate(board):
        for key_line, value_line in enumerate(value_board):
            if value_line == number_str:
                board[key_board][key_line] = player_str

create_board(board_size)
print(board)

modify_board("1","x")
modify_board("5","x")
modify_board("9","x")

print(board)
print("")

# Virkar fínt
def check_row_winner(board, player):
    for x in range(board_size):
        winner = True
        for y in range(board_size):
            if board[x][y] != player:                
                winner = False
                continue

        if winner == True:
            return winner
    return winner

def check_col_winner(board, player):
    for x in range(board_size):
        winner = True
        for y in range(board_size):
            if board[y][x] != player:                
                winner = False
                continue

        if winner == True:
            return winner
    return winner

def check_diag_winner(board, player):
    for x in range(board_size):
        winner = True
        for y in range(board_size):
            if board[x][x] != player:                
                winner = False
                continue
        return winner

print(check_col_winner(board,"X"))
print(check_row_winner(board,"X"))
print(check_diag_winner(board,"X"))

print("")
