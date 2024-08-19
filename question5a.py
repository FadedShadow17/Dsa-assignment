import random

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance_matrix[route[i]][route[(i + 1) % len(route)]]
    return total_distance

def generate_neighbor(route):
    neighbor = route[:]
    i, j = random.sample(range(len(route)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing_tsp(distance_matrix, max_iterations=1000):
    n = len(distance_matrix)
    current_route = list(range(n))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, distance_matrix)
    
    for iteration in range(max_iterations):
        neighbor_route = generate_neighbor(current_route)
        neighbor_distance = calculate_total_distance(neighbor_route, distance_matrix)
        
        if neighbor_distance < current_distance:
            current_route = neighbor_route
            current_distance = neighbor_distance
            print(f"Iteration {iteration}: Found better solution with distance {current_distance}")
    
    return current_route, current_distance

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, best_distance = hill_climbing_tsp(distance_matrix)
print("Best route found:", best_route)
print("Best distance:", best_distance)
