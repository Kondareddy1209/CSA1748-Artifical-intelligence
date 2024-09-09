class Node:
    def __init__(self, value=None, terminal=False):
        self.value = value  # Heuristic value for this node (for terminal nodes)
        self.terminal = terminal  # Is this node a terminal state?
        self.children = []  # List of child nodes

    def is_terminal(self):
        return self.terminal

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.get_children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  # Pruning occurs
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.get_children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:  # Pruning occurs
                break
        return min_eval

def build_tree():
    node_type = input("Is this a terminal node? (y/n): ").lower()

    if node_type == 'y':
        value = int(input("Enter the value of the node: "))
        return Node(value=value, terminal=True)
    
    node = Node(terminal=False)
    num_children = int(input("How many children does this node have?: "))

    for i in range(num_children):
        print(f"Creating child {i + 1} of {num_children}")
        child = build_tree()  # Recursively build child nodes
        node.children.append(child)

    return node

if __name__ == "__main__":
    print("Let's build the game tree manually!")
    root_node = build_tree()

    depth = int(input("Enter the depth of the search: "))
    result = alpha_beta_pruning(root_node, depth, float('-inf'), float('inf'), True)

    print(f"The optimal value is: {result}")
