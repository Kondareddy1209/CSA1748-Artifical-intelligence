def is_safe(graph, color, node, c):
    # Check if the color c is safe for node
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def map_coloring(graph, color, node, num_colors):
    # Base case: If all nodes are processed
    if node == len(graph):
        return True

    # Try different colors for node
    for c in range(1, num_colors + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if map_coloring(graph, color, node + 1, num_colors):
                return True
            # Backtrack
            color[node] = 0

    return False

def input_graph():
    print("Enter the adjacency matrix for the graph:")
    n = int(input("Enter the number of nodes: "))
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
        graph.append(row)
    return graph

def main():
    graph = input_graph()
    num_colors = int(input("Enter the number of colors: "))
    
    color = [0] * len(graph)
    if map_coloring(graph, color, 0, num_colors):
        print("Solution exists: Following are the assigned colors")
        for i in range(len(graph)):
            print(f"Node {i} -> Color {color[i]}")
    else:
        print("Solution does not exist")

if __name__ == "__main__":
    main()
