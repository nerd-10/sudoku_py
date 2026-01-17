#All sudoku related functions

def copy_board(board: list[list[int]]) -> list[list[int]]:
    """Create a deep copy of the Sudoku board."""
    return [row[:] for row in board]

def is_valid_move(board: list[list[int]], row: int, col: int, value: int) -> bool:
    """Check if placing value at (row,col) is valid accordind to Sudoku rules"""
    
    # can't overwrite a filled cell
    if board[row][col] != 0:
        return False
    
    #check row
    if value in board[row]:
        return False
    
    #check column
    for r in range(9):
        if board[r][col] == value:
            return False
        
    #check for 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3 
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == value:
                return False    
    return True

def is_board_complete(board: list[list[int]]) -> bool:
    """Return true if there is no empty cell in the board"""
    for row in board:
        if 0 in row:
            return False
    return True

def find_empty_cell(board: list[list[int]]) -> tuple[int, int] | None:
    """Return first empty cell positon or None if board is full"""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r,c)
    return None

