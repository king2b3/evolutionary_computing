"""Cannonical Genetic Algorithm (CGA)

A from scrath implementiation of a CGA, which is a genetic algorithm that works on a string of 0s and 1s only.

author: bking
date: 5/27/2025
"""

import numpy as np
#import matplotlib.pyplot as plt

# constants
POP_SIZE = 100
IND_LEN = 5
MUT_RATE = .01
GENERATIONS = 5000

# fitness
def fitness(pop):
    """returns the fitness of a population"""
    fit_pop = list(map(np.sum, pop))
    #normalize the fitness by the lenegth of each individual
    fit_pop_norm = np.divide(fit_pop, IND_LEN)
    return fit_pop_norm


# population functions
def generate_pop():
    #generates a random list from 0 to 1
    return np.random.randint(0,2,(POP_SIZE, IND_LEN))

def print_stats(pop):
    fit = fitness(pop)
    print(f'mean fitness: {np.mean(fit)}')
    print(f'min fitness: {np.min(fit)}')
    print(f'max fitness: {np.max(fit)}')
    print(f'% unique individuals in population: {(np.unique(pop, axis=0).shape[0] - 1) / POP_SIZE}')

def mutation(pop):
    """bit level mutation, for the whole population. each bit has the same
    chance to mutate, across all individuals, and all bits
    """
    #generate random numbers the same shape as the population
    mutation_probs = np.random.random((POP_SIZE, IND_LEN))
    #all values to be mutated are given the value of False
    #this allows for a very simple logical xor, to then mutate the selected value
    #the logical not wouldn't be needed if there was a logical xnor operation
    mutation_probs_masked = np.logical_not(mutation_probs >= MUT_RATE)
    mutated_pop = np.logical_xor(pop, mutation_probs_masked).astype(int)

    return mutated_pop

def crossover(pop):
    """Performs crossover for each element in the population.
    Single point crossover in this example
    """
    new_pop = []
    pop_len = len(pop)
    for _ in range(pop_len):
        parents = np.random.randint(pop_len, size=2)
        parent_1, parent_2 = pop[parents]
        #determine crossover point
        crossover_pt = np.random.choice(np.arange(IND_LEN))
        child_1 = np.hstack((parent_1[:crossover_pt], parent_2[crossover_pt:]))
        new_pop.append(child_1)
    new_pop = np.array(new_pop)
    return new_pop

def roulette_selection(pop, k=POP_SIZE):
    """Selection functions for the crossover individual"""
    #implement fitness based selection roulette wheel
    fitness_pop = fitness(pop)
    roulette_wheel = np.cumsum(fitness_pop)
    #normalize wheel between 0-1
    roulette_wheel = roulette_wheel / np.max(np.abs(roulette_wheel), axis=0)
    wheel_selection = np.random.random()
    parents = []
    for _ in range(k):
        parents.append(pop[np.searchsorted(roulette_wheel, wheel_selection)])

    if len(parents) == 1:
        return parents[0]
    return np.array(parents)


#### STARTING ####
population = generate_pop()

for g in range(GENERATIONS):
    print(f'generation: {g}')
    print_stats(population)
    parent_pool = roulette_selection(population)
    population = crossover(parent_pool)
    population = mutation(population)

    #check for exit conditions
    fit_pop = fitness(population)
    if ((np.unique(population, axis=0).shape[0] - 1) / POP_SIZE ) == 1.0 or np.min(fit_pop) == 1.0:
        print('#############')
        print('\n')
        print('#############')
        print_stats(population)
        break


breakpoint()
