def is_valid_state(state):
    m_left, c_left, boat, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    return True

def get_next_states(state):
    m_left, c_left, boat, m_right, c_right = state
    next_states = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, 'right', m_right + m, c_right + c)
        else:
            new_state = (m_left + m, c_left + c, 'left', m_right - m, c_right - c)
        if is_valid_state(new_state):
            next_states.append(new_state)
    return next_states

def missionaries_and_cannibals(m_start, c_start):
    start_state = (m_start, c_start, 'left', 0, 0)
    goal_state = (0, 0, 'right', m_start, c_start)
    visited = set()
    queue = [(start_state, [])]

    while queue:
        state, path = queue.pop(0)
        if state == goal_state:
            return path + [state]
        if state not in visited:
            visited.add(state)
            for next_state in get_next_states(state):
                queue.append((next_state, path + [state]))
    return None

def print_solution(solution):
    if solution:
        print("Solution found:")
        for i, state in enumerate(solution):
            m_left, c_left, boat, m_right, c_right = state
            print(f"Step {i}:")
            print(f"Left bank: {m_left}M {c_left}C")
            print(f"Right bank: {m_right}M {c_right}C")
            print(f"Boat is on the {'left' if boat == 'left' else 'right'}")
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    m_start = int(input("Enter the number of missionaries on the left bank: "))
    c_start = int(input("Enter the number of cannibals on the left bank: "))
    solution = missionaries_and_cannibals(m_start, c_start)
    print_solution(solution)
