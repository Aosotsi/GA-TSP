# Traveling Salesman Problem with Genetic Algorithm

This repository contains a Python implementation of a genetic algorithm to solve the Traveling Salesman Problem (TSP). The TSP is an NP-hard combinatorial optimization problem, where the goal is to find the shortest route for a salesman who needs to visit a set of cities and return to the starting city, visiting each city exactly once.

## Implementation

The genetic algorithm implemented in this project follows these steps:

1. Generate an initial population of random routes.
2. Evaluate the fitness of each route using the inverse of the total distance traveled.
3. Perform tournament selection to choose parents for reproduction.
4. Apply ordered crossover to generate offspring routes.
5. Introduce swap mutations to add diversity to the population.
6. Repeat steps 2-5 for a specified number of generations.
7. Return the best solution found in the final population.

The implementation is contained in the `GA.py` file, which defines the following functions:

- `fitness_function(route, distance_matrix)`: Calculates the fitness of a given route.
- `generate_initial_population(num_cities, population_size)`: Generates the initial population.
- `tournament_selection(population, fitness_function, distance_matrix, tournament_size)`: Selects parents using tournament selection.
- `ordered_crossover(parent_a, parent_b)`: Performs ordered crossover on two parent routes.
- `swap_mutation(route)`: Applies swap mutation to a given route.
- `genetic_algorithm(distance_matrix, population_size, num_generations, crossover_rate, mutation_rate, tournament_size)`: Main function to run the genetic algorithm.

## Usage

1. Clone the repository: 
git clone https://github.com/Aosotsi/tsp-genetic-algorithm.git
cd tsp-genetic-algorithm
2. Open the GA.py file and modify the distance_matrix variable to represent the pairwise distances between your cities.
3. Adjust the parameters for the genetic algorithm as needed, such as population_size, num_generations, crossover_rate, mutation_rate, and tournament_size.
4. Run the program: python GA.py
5. The program will output the best solution found by the genetic algorithm, in the form of a list of city indices.
