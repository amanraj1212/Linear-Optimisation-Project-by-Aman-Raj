# ga_app/genetic_algorithm.py
import random
import string

'''
def generate_random_string(length):
    random_chars = [random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, !') for _ in range(length)]
    return ''.join(random_chars)
'''
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    random_chars = [random.choice(characters) for _ in range(length)]
    return ''.join(random_chars)

def calculate_fitness(individual, target):
    return sum(1 for i, j in zip(individual, target) if i == j)

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        mutation_point = random.randint(0, len(individual) - 1)
        individual_list = list(individual)
        individual_list[mutation_point] = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, !')
        return ''.join(individual_list)
    return individual

def genetic_algorithm(target, mutation_rate, population_size, max_generations):
    population = [generate_random_string(len(target)) for _ in range(population_size)]
    generation = 0

    while generation < max_generations:
        fitness_scores = [calculate_fitness(individual, target) for individual in population]

        if max(fitness_scores) == len(target):
            max_fitness_score = max(fitness_scores)
            solution_index = fitness_scores.index(max_fitness_score)
            solution = population[solution_index]
            return f"Solution found: '{solution}' in generation {generation}"

        new_population = []

        for _ in range(population_size):
            parents = random.choices(population, weights=fitness_scores, k=2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        generation += 1

    return "Reached maximum generations without finding a solution."
