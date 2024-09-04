from heapq import heappop, heappush

# Define goal state
GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Define possible moves
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def print_board(state):
    """Print the board state in a human-readable format."""
    for row in state:
        print(' '.join(str(x) if x != 0 else '.' for x in row))
    print()

def heuristic(state):
    """Compute the Manhattan distance heuristic for the current state."""
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                goal_r, goal_c = divmod(value - 1, 3)
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def get_neighbors(state):
    """Generate all possible moves from the current state."""
    zero_r, zero_c = next((r, c) for r, row in enumerate(state) for c, val in enumerate(row) if val == 0)
    neighbors = []

    for dr, dc in MOVES:
        new_r, new_c = zero_r + dr, zero_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = [list(row) for row in state]
            new_state[zero_r][zero_c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[zero_r][zero_c]
            neighbors.append((tuple(tuple(row) for row in new_state), (new_r, new_c)))
    
    return neighbors

def a_star(start):
    """Solve the 8-puzzle problem using the A* algorithm."""
    open_list = []
    heappush(open_list, (0 + heuristic(start), 0, start, (None, None)))
    came_from = {}
    cost_so_far = {start: 0}
    solution = None

    while open_list:
        _, current_cost, current_state, move = heappop(open_list)

        if current_state == GOAL_STATE:
            solution = current_state
            break

        for neighbor, _ in get_neighbors(current_state):
            new_cost = current_cost + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heappush(open_list, (priority, new_cost, neighbor, _))
                came_from[neighbor] = current_state

    # Reconstruct path
    path = []
    while solution in came_from:
        path.append(solution)
        solution = came_from[solution]
    path.append(start)
    path.reverse()

    return path

def read_input():
    """Read the initial board configuration from the user."""
    print("Enter the initial board configuration (0 for empty space):")
    board = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != 3:
            raise ValueError("Each row must contain exactly 3 numbers.")
        board.append(tuple(row))
    return tuple(board)

def main():
    """Main function to run the 8-puzzle solver."""
    try:
        start = read_input()
        if sorted(num for row in start for num in row) != list(range(9)):
            raise ValueError("The board must contain all numbers from 0 to 8 exactly once.")
        path = a_star(start)
        for state in path:
            print_board(state)
        print(f"Total moves: {len(path) - 1}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
