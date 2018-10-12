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
print("")


modify_board("1","x")
modify_board("2","x")
modify_board("3","x")

#for p in range(board_size):
#    for key_line, value_line in enumerate(board[p]):
#        if board[p][key_line] == "X":
#            print(key_line,p)
#    

for n in range(board_size):
    pass

for x in range(board_size):
    for y in range(board_size):
        winner = True
        
        if board[y][x] != "X":
            winner = False
            continue
        if board[y][x] != "X":
            winner = False
            continue
        if board[x][x] != "X":
            winner = False
            continue
    
    if winner == True:
        print("We have a winner")

print("")
print(board)