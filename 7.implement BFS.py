from collections import deque

def get_user_input():
    """Get the grid, start, and goal positions from the user."""
    # Get grid dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize grid
    grid = []
    print("Enter the grid row by row (use 0 for open space and 1 for obstacles):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != cols:
            raise ValueError("Row length does not match the number of columns.")
        grid.append(row)

    # Get start and goal positions
    start_row = int(input("Enter the start row position: "))
    start_col = int(input("Enter the start column position: "))
    goal_row = int(input("Enter the goal row position: "))
    goal_col = int(input("Enter the goal column position: "))

    if not (0 <= start_row < rows) or not (0 <= start_col < cols):
        raise ValueError("Start position is out of bounds.")
    if not (0 <= goal_row < rows) or not (0 <= goal_col < cols):
        raise ValueError("Goal position is out of bounds.")

    return grid, (start_row, start_col), (goal_row, goal_col)

def bfs(grid, start, goal):
    """Perform BFS to find the shortest path from start to goal."""
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(*start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current_row, current_col, path = queue.popleft()

        if (current_row, current_col) == goal:
            return path

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            if (0 <= new_row < rows) and (0 <= new_col < cols) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, path + [(new_row, new_col)]))

    return None

def print_path(path):
    """Print the path from start to goal."""
    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found.")

def main():
    try:
        grid, start, goal = get_user_input()
        path = bfs(grid, start, goal)
        print_path(path)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
