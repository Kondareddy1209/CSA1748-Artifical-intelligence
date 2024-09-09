from itertools import permutations

def travelling_salesman(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    best_path = None
 
    for perm in permutations(vertices):
        current_path = [start] + list(perm) + [start]
        try:
            current_cost = sum(graph[current_path[i]][current_path[i + 1]] for i in range(len(current_path) - 1))
        except KeyError as e:
            print(f"Error: Missing path {e}. Please check the connections.")
            continue

        if current_cost < min_path:
            min_path = current_cost
            best_path = current_path

    return best_path, min_path

# Input the graph
n = int(input("Enter number of cities: "))
graph = {}
for _ in range(n):
    city = input("Enter city name: ")
    graph[city] = {}
    num_neighbors = int(input(f"Enter number of neighbors for {city}: "))  # Expect an integer here!
    
    for _ in range(num_neighbors):
        neighbor = input(f"Enter neighboring city for {city}: ")
        
        while True:
            try:
                cost = int(input(f"Enter cost from {city} to {neighbor}: "))  # Expect an integer cost here
                break
            except ValueError:
                print("Invalid cost! Please enter a numeric value.")
        
        graph[city][neighbor] = cost

        # Make the graph bidirectional by adding the reverse path
        if neighbor not in graph:
            graph[neighbor] = {}
        graph[neighbor][city] = cost

# Display the graph structure for debugging
print("\nGraph structure:")
for city, neighbors in graph.items():
    print(f"{city}: {neighbors}")

start = input("Enter starting city: ")
path, cost = travelling_salesman(graph, start)
if path:
    print(f"Best path: {path}, Cost: {cost}")
else:
    print("No valid path found due to missing connections.")
