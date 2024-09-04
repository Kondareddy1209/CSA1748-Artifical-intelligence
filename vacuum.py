class VacuumCleaner:
    def __init__(self, grid, start_row, start_col):
        self.grid = grid
        self.row = start_row
        self.col = start_col
        self.moves = []

    def clean(self):
        """Clean the room using a simple strategy."""
        def in_bounds(r, c):
            return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])

        def move_to(r, c):
            if in_bounds(r, c):
                self.row, self.col = r, c
                self.moves.append((r, c))
                if self.grid[r][c] == 1:
                    print(f"Cleaning cell ({r}, {c})")
                    self.grid[r][c] = 0

        # Simple strategy: move in a spiral-like pattern or a defined pattern
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for _ in range(len(self.grid) * len(self.grid[0])):
            if self.grid[self.row][self.col] == 1:
                move_to(self.row, self.col)
            for dr, dc in directions:
                new_row, new_col = self.row + dr, self.col + dc
                if in_bounds(new_row, new_col) and self.grid[new_row][new_col] == 1:
                    move_to(new_row, new_col)
                    break

        print("Cleaning completed.")
        print("Path taken:", self.moves)
        print("Final grid:")
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

def get_user_input():
    """Get the grid and initial position from the user."""
    # Get grid dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize grid
    grid = []
    print("Enter the grid row by row (use 0 for clean and 1 for dirty):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != cols:
            raise ValueError("Row length does not match the number of columns.")
        grid.append(row)

    # Get initial position
    start_row = int(input("Enter the initial row position: "))
    start_col = int(input("Enter the initial column position: "))

    if not (0 <= start_row < rows) or not (0 <= start_col < cols):
        raise ValueError("Initial position is out of bounds.")

    return grid, start_row, start_col

def main():
    try:
        grid, start_row, start_col = get_user_input()
        vacuum = VacuumCleaner(grid, start_row, start_col)
        vacuum.clean()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
