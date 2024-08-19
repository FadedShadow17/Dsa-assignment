import random
import math

def calculate_distance(city1, city2):
    return math.dist(city1, city2)

def compute_total_distance(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

def create_initial_solution(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

def create_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            neighbor = tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def solve_tsp_with_hill_climbing(cities):
    num_cities = len(cities)
    current_solution = create_initial_solution(num_cities)
    current_distance = compute_total_distance(current_solution, cities)

    while True:
        neighbors = create_neighbors(current_solution)
        best_neighbor = min(neighbors, key=lambda tour: compute_total_distance(tour, cities))
        best_distance = compute_total_distance(best_neighbor, cities)

        if best_distance >= current_distance:
            break

        current_solution, current_distance = best_neighbor, best_distance

    return current_solution, current_distance

cities = [
    (0, 0), (1, 3), (4, 3), (6, 1),
    (3, 0), (2, 4), (5, 5), (7, 2)
]

best_tour, best_distance = solve_tsp_with_hill_climbing(cities)
print("Best tour found:", best_tour)
print("Total distance of the best tour:", best_distance)

