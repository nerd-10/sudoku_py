#Board printing and input handling utilities for a Sudoku game
#from puzzles import puzzles

def print_board(board: list[list[int]]): 
    """Print the Sudoku board in a readable format."""
    for r in range(9):
        if r % 3 == 0 and r!=0:
            print(" -"*10) #prntining horizontal separator every 3 rows
        row = [] 

        for c in range(9):
            if c % 3 == 0 and c!= 0:
               row.append("|") #printing vertical separator every 3 columns

            val = board[r][c]

            row.append(str(val) if val != 0 else ".")

        print(" ".join(row))
#print_board(puzzles[0])  # Example usage with the first puzzle

def get_user_input() -> tuple[int, int, int] | None:
    print("The input format is row column value.")
    while True:
        move = input("Please enter move(row col value) or q to quit: ").strip().lower()
        if move == "q":
            return None
        
        move_parts = move.split()
        if len(move_parts) != 3:
            print("Format should be: row col value, for examople: 3 4 5")
            continue
    
        try:
            row = int(move_parts[0]) - 1
            col = int(move_parts[1]) - 1
            value = int(move_parts[2])

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue 

        if row not in range(9) or col not in range(9) or value not in range(0, 10):
            print("Invalid input. Please enter numbers between 1 and 9 or 0 to clear.")
            continue

        return (row, col, value)