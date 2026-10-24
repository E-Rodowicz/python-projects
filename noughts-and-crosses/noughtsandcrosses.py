'''
A (hopefully) unbeatable game of noughts and crosses. User vs Computer AI.
'''
import random
import os.path
import json
random.seed(0)

def draw_board(board):
    '''Draws the board'''
    print("                  ----------- ")
    print("                 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("                  ----------- ")
    print("                 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("                  ----------- ")
    print("                 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("                  ----------- ")

def welcome(board):
    '''
    Prints the welcome message.
    Displays the board by calling draw_board(board).
    '''
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is show below:')
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    '''Turns everything on the board into an empty space.'''
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def get_player_move(board):
    '''
    Asks the user for input and assists by displaying the input numbers of the grid.
    Checks each col in row, and if the space is occupied,
    tells the players that the move is invalid and loops.
    If valid, returns row and col coordinates.
    '''
    while True:
        try:
            print("                   1   2   3")
            print("                   4   5   6")
            choice = int(input("Choose yor square: 7   8   9 : "))

            if choice < 1 or choice > 9:
                print("Invalid choice, please choose an unoccupied number between 1 and 9.")
                draw_board(board)
                continue

            if choice in [1, 2, 3] and board[0][choice - 1] == ' ':
                row = 0
                col = choice - 1
                break

            if choice in [4, 5, 6] and board[1][choice - 4] == ' ':
                row = 1
                col = choice - 4
                break
            if choice in [7, 8, 9] and board[2][choice - 7] == ' ':
                row = 2
                col = choice - 7
                break

        except ValueError:
            print("Invalid choice, please choose an unoccupied number between 1 and 9.")
            draw_board(board)
            continue
    return row, col

def choose_computer_move(board):
    '''
    The computer AI. It decides where to move next. I've made it as optimal as possible,
    so I don't think it can be beaten — only drawn.
    Its first priority is to check for potential winning moves.
    '''
    # ---Checks the rows for a potential win---

    # Note: Rows and columns come first before diagonals in every instance as
    # they are statistically superior in terms of winning.
    for row in range(3):
        if board[row].count("O") == 2 and board[row].count(" ") == 1:
            col = board[row].index(" ")
            return row, col

    # Checks the columns for a potential win.
    for col in range(3):
        current_col = [board[row][col] for row in range(3)]
        if current_col.count("O") == 2 and current_col.count(" ") == 1:
            row = current_col.index(" ")
            return row, col

    # Checks the left to right diagonal for a potential win.
    l_diag = [board[0][0], board[1][1], board[2][2]]
    if l_diag.count("O") == 2 and l_diag.count(" ") == 1:
        col = l_diag.index(" ")
        row = col
        return row, col

    # Checks the right to left diagonal for a potential win.
    r_diag = [board[0][2], board[1][1], board[2][0]]
    if r_diag.count("O") == 2 and r_diag.count(" ") == 1:
        row = r_diag.index(" ")
        col = 2 - row
        return row, col

    # ---Next, it attemps to block the player from winning.---

    # Checks which rows are in danger.
    for row in range(3):
        if board[row].count("X") == 2 and board[row].count(" ") == 1:
            col = board[row].index(" ")
            return row, col

    # Checks which columns are in danger.
    for col in range(3):
        current_col = [board[row][col] for row in range(3)]
        if current_col.count("X") == 2 and current_col.count(" ") == 1:
            row = current_col.index(" ")
            return row, col

    # Checks if the left to right diagonal is in danger.
    l_diag = [board[0][0], board[1][1], board[2][2]]
    if l_diag.count("X") == 2 and l_diag.count(" ") == 1:
        col = l_diag.index(" ")
        row = col
        return row, col

    # Checks if the right to left diagonal is in danger.
    r_diag = [board[0][2], board[1][1], board[2][0]]
    if r_diag.count("X") == 2 and r_diag.count(" ") == 1:
        row = r_diag.index(" ")
        col = 2 - row
        return row, col

    # ---After wins and blocks are checked, next comes the strategy.---

    # This is a "fork" - it attempts to win by creating two threats at the
    # same time in which case only one can be blocked.
    # If the computer has the center and the user took a corner,
    # the computer takes the opposite corner to set up a "fork".
    if board[1][1] == 'O':
        if board[0][0] == 'X' and board[2][2] == ' ':
            return 2, 2
        if board[0][2] == 'X' and board[2][0] == ' ':
            return 2, 0
        if board[2][0] == 'X' and board[0][2] == ' ':
            return 0, 2
        if board[2][2] == 'X' and board[0][0] == ' ':
            return 0, 0

    # This attemps to block any "fork" attemps made by the user.
    # If the user has two corners opposite each other, the computer takes a non-corner edge.
    if board[0][0] == 'X' and board[2][2] == 'X':
        if board[0][1] == ' ':
            return 0, 1
        if board[1][0] == ' ':
            return 1, 0
    if board[0][2] == 'X' and board[2][0] == 'X':
        if board[0][1] == ' ':
            return 0, 1
        if board[1][2] == ' ':
            return 1, 2

    # If none of the above apply and the centre is free, it simply takes the centre
    # due to its advantageous position.
    if board[1][1] == ' ':
        return 1, 1

    # If the player has a corner, the computer takes the opposite corner.
    if board[0][0] == 'X' and board[2][2] == ' ':
        return 2, 2
    if board[0][2] == 'X' and board[2][0] == ' ':
        return 2, 0
    if board[2][0] == 'X' and board[0][2] == ' ':
        return 0, 2
    if board[2][2] == 'X' and board[0][0] == ' ':
        return 0, 0

    # Computer takes a corner if one if free and nothing above is available.
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in corners:
        row, col = corner
        if board[row][col] == ' ':
            return row, col

    # Computer takes any available non-corner edge.
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for row, col in edges:
        if board[row][col] == ' ':
            return row, col

    # If somehow none of the above apply, it picks a random position on the board
    # (Should not even get to this!).
    empty = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty.append((row, col))

    if empty:
        row, col = random.choice(empty)
        return row, col

def check_for_win(board, mark):
    '''
    Checks if user/computer has won the game by checking if there are three X/O marks
    in a row/column/diagonal line.
    '''
    # Checks all rows for a win.
    for row in range(3):
        if board[row].count(mark) == 3:
            return True

    # Checks all columns for a win.
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(mark) == 3:
            return True

    # Checks diagonal left to right for a win.
    l_diag = [board[0][0], board[1][1], board[2][2]]
    if l_diag.count(mark) == 3:
        return True

    # Checks diagonal right to left for a win.
    r_diag = [board[0][2], board[1][1], board[2][0]]
    if r_diag.count(mark) == 3:
        return True

    #If there is no win, it returns False.
    return False

def check_for_draw(board):
    '''
    Checks for a draw by counting if every space if filled. If yes, it returns True.
    If it finds an empty space, it returns False.
     '''
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

def play_game(board):
    '''
    Calls in all required functions for the game to functions.
    First it clears the board to empty spaces and gives the user the first move.
    After, the user picks his move, the computer is called to do its move.
    This continues in a loop. After each move, win and draw conditions are checked
    and an appropriate value is returned if one of those conditions is met.
    '''
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You win!")
            return 1
        if check_for_draw(board):
            print("You drew.")
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0

def menu():
    '''
    Gets user input of either "1", "2", "3" or "q".
    Loops until one of those inputs is typed in.
    '''
    while True:
        choice = input(
            "Enter one of the following options:\n"
            "     1 - Play Game\n"
            "     2 - Save Score to Leaderboard\n"
            "     3 - Load and Display Leaderboard\n"
            "     q - End the Program\n"
        )
        if choice not in ("1", "2", "3", "q"):
            print("Invalid input. Please try again.")
        else:
            return choice

def load_scores():
    '''
    This loads the leaderboard.txt file and converts it into a Python
    dictionary called "leaders" for use within other functions.
    '''
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r", encoding="utf-8") as file_handle:
            leaders = json.load(file_handle)
    else:
        leaders = {}
    return leaders

def save_score(score):
    '''Writes your current total score into the leaderboard.txt file.'''
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open("leaderboard.txt", 'w', encoding="utf-8") as file_handle:
        json.dump(leaders, file_handle)
    return

def display_leaderboard(leader_board):
    '''
    Displays the current leaderboard stored in the leaderboard.txt file
    (Which is converted into a Python dictionary by the load_scores function.)
    '''
    print("\nCurrent Leaderboard")
    print("  -------------------")
    if not leader_board:
        print("No scores yet!")
    else:
        for name, score in leader_board.items():
            print(f"{name}: {score}")
        print("\n")
