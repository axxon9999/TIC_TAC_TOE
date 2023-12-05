import random

player1 = ''
player2 = ''
players = [player1, player2]

# -------------------RESET BOARD------------------


def reset_board():
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board

# --------------------INTRO---------------------------


def intro():
    print('\n' * 100)
    print('-----------------------')
    print('Welcome to Tic Tac Toe!')
    print('-----------------------')
    print('''Use numpad to match grid location:

     7 | 8 | 9  
    ----------- 
     4 | 5 | 6  
    ----------- 
     1 | 2 | 3 
     ''')
    players[0] = input('Player 1, what is your first name? ')
    players[1] = input('Player 2, what is your first name? ')
    return players

# -----DISPLAY BOARD ------------------------------------


def display_board(board):
    print("\n" * 100)
    print("")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print(f"--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"--+---+--")
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("")

# -----PLAYER INPUT ---------------------------------------


def player_input(first_player):
    marker_choice = ''

    while marker_choice != 'X' and marker_choice != 'O':
        marker_choice = input(f"{first_player}: Do you want to be X or O? ")

    return marker_choice

# --------PLACE MARKER----------------------------


def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)

# ---------CHECK FOR A WIN-------------------------------------


def win_check(board, mark):
    win = False
    if board[1] == board[2] == board[3] == mark:
        win = True
    elif board[4] == board[5] == board[6] == mark:
        win = True
    elif board[7] == board[8] == board[9] == mark:
        win = True
    elif board[1] == board[4] == board[7] == mark:
        win = True
    elif board[2] == board[5] == board[8] == mark:
        win = True
    elif board[3] == board[6] == board[9] == mark:
        win = True
    elif board[7] == board[5] == board[3] == mark:
        win = True
    elif board[1] == board[5] == board[9] == mark:
        win = True
    return win

# ---------------WHO PLAY FIRST---------------------------------


def choose_first():
    num = random.randint(1, 2)
    if num == 1:
        print(f'{players[0]} plays first!')
        return players[0]
    else:
        print(f'{players[1]} plays first!')
        return players[1]

# --------------LOOK FOR FREE SPACE ON THE BOARD--------------------------------


def space_check(board, position):
    return board[position] == ' '

# ----------------LOOK FOR A FULL BOARD -----------------------------------------


def full_board_check(board):
    return ' ' not in board

# ----------------------PLAYER CHOOSE A LOCATION--------------------


def player_choice(board, first_player):
    position = 0
    while position < 1 or position > 9:
        position = input(f"{first_player}, please select a position on the board (1-9): ")
        if position.isalpha():
            position = 0
        position = int(position)
        if position < 1 or position > 9:
            position = 0
        elif space_check(board, position):
            return position
        else:
            position = 0

# -------------------- PLAY AGAIN ? -----------------------------


def replay():
    play_again = 0
    while play_again != 'y' and play_again != 'n':
        play_again = input("Do you want to play again? (Y/N) ").lower()
        if play_again == 'y':
            start()
        elif play_again == 'n':
            print('Goodbye!')
            exit()

# ---------------------ARE YOU READY?--------------------------


def are_you_ready():
    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = input("Are you ready to play? (Y/N) ").lower()
        if play_again == 'y':
            pass
        elif play_again == 'n':
            print('Goodbye!')
            exit()

# ------------------PLAY THE GAME------------------------------


def play_game(first_player, marker_choice, board):
    x = True
    while x:

        position = player_choice(board, first_player)
        place_marker(board, marker_choice, position)

        if win_check(board, marker_choice):
            x = False
            print(f'{first_player} wins!')
            replay()
        if full_board_check(board):
            x = False
            print('The board is full, no winner.')
            replay()

        first_player = switch_player(first_player)
        marker_choice = switch_marker(marker_choice)

# ---------------------SWITCH PLAYER AND MARKER---------------------------


def switch_player(first_player):
    if first_player == players[0]:
        first_player = players[1]
    else:
        first_player = players[0]

    return first_player


def switch_marker(marker_choice):
    if marker_choice == 'X':
        marker_choice = 'O'
    else:
        marker_choice = 'X'
    return marker_choice

# ---------------------GAME ENGINE------------------------------


def start():
    while True:
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        intro()
        first_player = choose_first()
        marker_choice = player_input(first_player)
        are_you_ready()
        play_game(first_player, marker_choice, board)

# -------------------------------------------------------------


start()
