import random
from puzzles import puzzles
from utils import print_board, get_user_input
from sudoku import  copy_board, is_valid_move, is_board_complete

def main():
    print("Welcome to predetermined Sudoku!")
    # Choose a puzzle at random
    puzzle = random.choice(puzzles)

    #make a working board
    board = copy_board(puzzle)

    #make a fixed board to track original values
    fixed_board = copy_board(puzzle)

    while True:
        print_board(board)

        if is_board_complete(board):
            print("Congratulations!")
            break

        user_move = get_user_input()
        if user_move is None:
            print("Thank you for playing! Goodbye!")
            break
        row, col, value = user_move

        if fixed_board[row][col]!= 0:
            print("Cannot change the original puzzle values. Try again.")
            continue

        # allow clearing a cell
        if value == 0:
            board[row][col] = 0
            print("Cell cleared.")
            continue


        if is_valid_move(board, row, col, value):
            board[row][col] = value
        else:
            print("Invalid move. Try again.") 
        
if __name__ == "__main__":
    main()
# Run the main function to start the game

