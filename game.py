def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic Tac Toe!")

    while not game_over:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            else:
                if " " not in [cell for row in board for cell in row]:
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    main()
