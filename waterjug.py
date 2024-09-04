from collections import deque

def water_jug_problem(a, b, d):
    """Find the steps to measure exactly d liters using two jugs with capacities a and b."""
    if d > max(a, b):
        return "Not possible"
    
    def get_neighbors(state):
        """Generate all possible states from the current state."""
        x, y = state
        neighbors = []

        # Fill jug 1
        neighbors.append((a, y))
        # Fill jug 2
        neighbors.append((x, b))
        # Empty jug 1
        neighbors.append((0, y))
        # Empty jug 2
        neighbors.append((x, 0))
        # Pour jug 1 into jug 2
        pour = min(x, b - y)
        neighbors.append((x - pour, y + pour))
        # Pour jug 2 into jug 1
        pour = min(y, a - x)
        neighbors.append((x + pour, y - pour))

        return neighbors

    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    parent = { (0, 0): None }  # To reconstruct the path

    while queue:
        current_state = queue.popleft()
        if current_state[0] == d or current_state[1] == d:
            break

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_state
                queue.append(neighbor)

    # Reconstruct the path
    if current_state[0] != d and current_state[1] != d:
        return "Not possible"

    path = []
    while current_state:
        path.append(current_state)
        current_state = parent[current_state]
    path.reverse()

    return path

def print_solution(path):
    """Print the sequence of steps to solve the problem."""
    for state in path:
        print(f"Jug 1: {state[0]} liters, Jug 2: {state[1]} liters")
    print()

# Get user input
a = int(input("Enter the capacity of jug 1 (in liters): "))
b = int(input("Enter the capacity of jug 2 (in liters): "))
d = int(input("Enter the desired amount of water (in liters): "))

solution_path = water_jug_problem(a, b, d)
if solution_path == "Not possible":
    print(solution_path)
else:
    print("Steps to measure exactly", d, "liters:")
    print_solution(solution_path)
