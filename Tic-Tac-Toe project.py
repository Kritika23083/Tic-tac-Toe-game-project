# Tic-Tac-Toe

# Create the game board
board = [" " for _ in range(9)]

# Function to print the game board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if any player has won
def check_win(player):
    # Check rows
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player)
    ):
        return True

    # Check columns
    if (
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player)
    ):
        return True

    # Check diagonals
    if (
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True

    return False

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    current_player = "X"
    game_over = False

    while not game_over:
        position = int(input("Choose a position (1-9): ")) - 1

        if board[position] == " ":
            board[position] = current_player
            print_board()

            if check_win(current_player):
                print("Congratulations! Player", current_player, "wins!")
                game_over = True
            elif " " not in board:
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already filled. Choose a different position.")

# Start the game
play_game()
