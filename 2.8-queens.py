def print_board(board):
    """Print the chessboard with queens and include the number of queens."""
    size = len(board)
    queen_count = sum(sum(row) for row in board)  # Count the number of queens
    print(f"Number of queens: {queen_count}")
    for row in board:
        print(' '.join('Q' if cell else '.' for cell in row))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    # Check this column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False

    return True

def solve_queens(board, row, solutions):
    """Solve the N-Queens problem using backtracking and count solutions."""
    if row >= len(board):
        print_board(board)
        solutions[0] += 1
        return True

    solved = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            solved = solve_queens(board, row + 1, solutions) or solved
            board[row][col] = False

    return solved

def main():
    """Initialize the chessboard and solve the N-Queens problem."""
    size = int(input("Enter the number of queens (and the size of the board): "))
    board = [[False] * size for _ in range(size)]
    solutions = [0]  # Use a list to keep a mutable count of solutions

    if not solve_queens(board, 0, solutions):
        print("No solution exists.")
    
    print(f"Total number of solutions: {solutions[0]}")

if __name__ == "__main__":
    main()
