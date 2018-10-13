board = []
board_size = 3

# Creates the board and the size of the board
def create_board(board_size):
    t = 1
    for i in range(1,board_size+1):
        line = []
        for j in range(1,board_size+1):
            line.append(str(t))
            t += 1
        board.append(line)

# Check if select number exists
def check_if_number_exists(number):
    number_exists = False
    for key, value in enumerate(board):
        if str(number) in value:
            number_exists = True
    return number_exists

# Modify the board based on player selection
def modify_board(number, player):
    player_str = str(player).upper()
    number_str = str(number)
    if check_if_number_exists(number) == True:
        for key_board, value_board in enumerate(board):
            for key_line, value_line in enumerate(value_board):
                if value_line == number_str:
                    board[key_board][key_line] = player_str
    else:
        print("Illegal move!")

create_board(board_size)
print(board)

modify_board("1","x")
modify_board("2","x")
modify_board("3","o")
modify_board("4","o")
modify_board("5","o")
modify_board("6","x")
modify_board("7","x")
modify_board("8","x")
modify_board("9","o")

print(board)
print("")

# Check each row if there is a win
def check_row_winner(player):
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
def check_col_winner(player):
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
def check_dia_winner_lr(player):
    winner = False
    counter_dia = 0

    for x in range(len(board)):
        if board[x][x] == player:
            counter_dia += 1

        if counter_dia == len(board):
            winner = True
    return winner

# Checks diagonal rows from left to right
def check_dia_winner_rl(player):
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

# Check if draw
def check_draw():
    number_exists = False
    for key_board, value_board in enumerate(board):
        for key_line, value_line in enumerate(value_board):
            try:
                if int(value_line):
                    number_exists = True
            except ValueError:
                pass
    return number_exists

# Evaluates the board and then figures out who is the winner
# Returns two variables, eather if there is a draw or if there is a winner.
def check_winner_board(player):
    is_winner = False
    is_draw = False
    if check_row_winner(player) == True or check_col_winner(player) == True or check_dia_winner_lr(player) == True or check_dia_winner_rl(player) == True:
        is_winner = True
    else:
        is_winner = False
    if is_winner == False:
        if check_draw() == False:
            is_draw = True
            print("Draw!")
    return is_winner, is_draw

print(check_winner_board("X"))
