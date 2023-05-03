import numpy as np
from itertools import permutations
import random

def fitness_function(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        city_a = route[i]
        city_b = route[i + 1]
        total_distance += distance_matrix[city_a, city_b]
    total_distance += distance_matrix[route[-1], route[0]]  # Return to the starting city
    fitness = 1 / total_distance
    return fitness

def generate_initial_population(num_cities, population_size):
    all_permutations = list(permutations(range(1, num_cities)))  # Exclude the starting city (0)
    initial_population = [random.choice(all_permutations) for _ in range(population_size)]
    initial_population = [list(route) for route in initial_population]
    return initial_population


def tournament_selection(population, fitness_function, distance_matrix, tournament_size):
    selected = []
    for _ in range(tournament_size):
        candidate = random.choice(population)
        if not selected or fitness_function(candidate, distance_matrix) > fitness_function(selected, distance_matrix):
            selected = candidate
    return selected

def ordered_crossover(parent_a, parent_b):
    size = len(parent_a)
    start, end = sorted(random.sample(range(size), 2))

    child = [None] * size
    child[start:end] = parent_a[start:end]

    available_positions = [i for i in range(size) if i < start or i >= end]
    for city in parent_b:
        if city not in child:
            child[available_positions.pop(0)] = city

    return child

def swap_mutation(route):
    mutated = route.copy()
    index_a, index_b = random.sample(range(len(mutated)), 2)
    mutated[index_a], mutated[index_b] = mutated[index_b], mutated[index_a]
    return mutated

def genetic_algorithm(distance_matrix, population_size, num_generations, crossover_rate, mutation_rate, tournament_size):
    # Generate the initial population
    population = generate_initial_population(len(distance_matrix), population_size)

    # Main loop
    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size):
            # Selection
            parent_a = tournament_selection(population, fitness_function, distance_matrix, tournament_size)
            parent_b = tournament_selection(population, fitness_function, distance_matrix, tournament_size)

            # Crossover
            if random.random() < crossover_rate:
                offspring = ordered_crossover(parent_a, parent_b)
            else:
                offspring = parent_a

            # Mutation
            if random.random() < mutation_rate:
                offspring = swap_mutation(offspring)

            new_population.append(offspring)

        population = new_population

    # Find the best solution in the final population
    best_solution = max(population, key=lambda route: fitness_function(route, distance_matrix))
    return best_solution

distance_matrix = np.array([
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 14],
    [10, 3, 0, 6, 20],
    [19, 7, 6, 0, 4],
    [8, 14, 20, 4, 0]
])

population_size = 50
num_generations = 100
crossover_rate = 0.8
mutation_rate = 0.1
tournament_size = 5

best_solution = genetic_algorithm(distance_matrix, population_size, num_generations, crossover_rate, mutation_rate, tournament_size)

print(f"Best solution: {best_solution}")

