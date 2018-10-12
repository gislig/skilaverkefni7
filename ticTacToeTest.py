
board = []

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
    for key_board, value_board in enumerate(board):
        for key_line, value_line in enumerate(value_board):
            if value_line == number:
                board[key_board][key_line] = player_str

create_board(3)
print(board)

modify_board("9","o")
modify_board("1","x")
modify_board("4","X")
modify_board("7","X")

#for key_board, value_board in enumerate(board):
#   if value_board[0] == "X":
#       print(value_board[0])

[i for i, j in zip(a, b) if i == j]
    
print(board)


print(board)