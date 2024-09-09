def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Input the graph
n = int(input("Enter number of nodes: "))
graph = {}
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")
dfs(graph, start)
