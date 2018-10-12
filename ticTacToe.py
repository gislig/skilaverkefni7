def board_dimensions():
    """ Create the board dimensions """
    dimension_str = input("Input dimension of the board: ")
    pass

def player_turn(turn):
    """ Check each players turn """
    if turn == "":
        selected_str = input("X position: ")
    else:
        selected_str = input("O position: ")
    return int(selected_str)

def check_winner():
    """ Check if the game is over and who is the winner or if it is a tie """
    pass

def board_selection(position):
    """ Select the possition of the board and mark it with O or X """
    pass

def main():
    pass

main()