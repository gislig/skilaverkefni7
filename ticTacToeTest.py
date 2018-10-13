board = []
board_size = 4

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
modify_board("13","x")

print(board)
print("")

# Check each row if there is a win
def check_row_winner(board, player):
    winner = False
    for x in range(len(board)):
        counter_row = 0
        for y in range(len(board)):
            if board[x][y] == player:
                counter_row += 1
                if counter_row == len(board):
                    winner = True
                continue
    return winner

# Checks columns down if there is a win
def check_col_winner(board, player):
    winner = False
    for x in range(len(board)):
        counter_col = 0
        for y in range(len(board)):
            if board[y][x] == player:
                counter_col += 1
                if counter_col == len(board):
                    winner = True
                continue
    return winner

# Checks diagonal rows from left to right
def check_dia_winner_lr(board, player):
    winner = False
    counter_dia = 0

    for x in range(len(board)):
        if board[x][x] == player:
            counter_dia += 1

        if counter_dia == len(board):
            winner = True
    return winner

# Checks diagonal rows from left to right
def check_dia_winner_rl(board, player):
    winner = False
    counter_dia = 0
    reverse_count = 0
    for x in reversed(range(len(board))):
        
        if board[x][reverse_count] == player:
            counter_dia += 1
        reverse_count += 1

        if counter_dia == len(board):
            winner = True
    return winner

# Evaluates the board and then figures out who is the winner
def check_winner_board(board, player):
    if check_row_winner(board,player) == True or check_col_winner(board,player) == True or check_dia_winner_lr(board,player) == True or check_dia_winner_rl(board,player) == True:
        return True
    else:
        return False

print(check_winner_board(board,"X"))
