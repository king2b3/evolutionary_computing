import argparse
import os

def parse_arguments(args=None) -> None:
    '''Returns the parsed arguments.

    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    '''
    parser = argparse.ArgumentParser(description='General genetic framework',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('population_size', type=int,
            help='Initial size of the population.')
    parser.add_argument('individual_size', type=int,
            help='Size of the genome of each individual.')
    parser.add_argument('-is','--individual_split', type=int, default=1,
            help='Number of variables in the individual genome.')
    parser.add_argument('-f','--fit', type=str, default="max_ones",
            help='Pick the fitness function type. Options: rosenbrock, max_ones, himmelblau_max, himmelblau_min')
    parser.add_argument('-mg','--max_gens', default=2000, type=int,
            help='Maximum number of generations allowed')
    parser.add_argument('-cr','--cross_over_rate', default=0.5, type=float,
            help='Crossover rate. Options in range [0,1]')
    parser.add_argument('-mr','--mutation_rate', default=0.001, type=float,
            help='Mutation rate. Options in range [0,1]')
    parser.add_argument('-s','--selection_type', default='roulette',
            help='The type of selection function used. Options: random, roulette, tournament.')
    parser.add_argument('-k', default=1, type=int,
            help='K-point crossover. Options in range [1:Genome Size - 1]')
    parser.add_argument('-p', '--pop', default="fixed", type=str,
            help='Population type. Options: fixed, mew_lambda')
    args = parser.parse_args(args=args)
    return args

def main(population_size, individual_size, individual_split, fit, cross_over_rate,
                mutation_rate, k, max_gens, selection_type, pop) -> None:
    '''Main function.

    Parameters
    ----------
    population_size: int:
        Size of the initial population.
    individual_size: int:
        Size of the genome of the individual.
    individual_split: int:
        Number of variables in the individual genome.
    fitness: str:
        The fitness function we are testing.
    max_gens: int:
        Maximum number of generations allowed during the evolutionary process.
    cross_over_rate: float:
        The rate of crossover.
    mutation_rate: float:
        The rate of mutation.
    selection_type: str:
        The selection type.
    k: int:
        The number of crossover points

    Returns
    ------- 
        None
    
    Raises
    ------
        None yet, if incorrect args are used eventually
    '''    
    # imports
    """class imports based off of arg parsing"""
    # fitness
    if fit == 'rosenbrock':
        from ga.fitness import RosenbrockFixed as fitness
        maxFit = False
        best_m = 999999
        best_a = 999999
        best_per = 999999
    elif fit == 'max_ones':
        from ga.fitness import MaxOnes as fitness
        maxFit = True
        best_m = 0
        best_a = 0
        best_per = 0
    elif fit == 'himmelblau_max':
        from ga.fitness import HimmelblauMax as fitness
        maxFit = True
        best_m = 0
        best_a = 0
        best_per = 0
    else: #if fit == 'himmelblau_max':
        from ga.fitness import HimmelblauMin as fitness
        maxFit = False
        best_m = 999999
        best_a = 999999
        best_per = 999999
    # selection
    if selection_type == 'random':
        from ga.selection import Random as selection
    elif selection_type == 'tournament':
        from ga.selection import Tournament as selection
    elif selection_type == 'uniform':
        from ga.selection import UniformRandom as selection
    else:
        from ga.selection import RouletteWheelSelection as selection
    # population type
    if pop == 'fixed':
        from ga.population import FixedSize as population 
    else:
        from ga.population import MewLambda as population
    # my custom timer class
    from timer import Timer
    # Other imports    
    from tabulate import tabulate   # pretty plotting
    from os import system           # for clearing the terminal
    import random                   # random library
    random.seed()                   # seeding the random num gengerator

    def clear():
        _ = system("clear")
    
    clear()    

    if individual_split > 1:
        individual_split = int(individual_size/individual_split)
    #print(individual_split)
    
    print_list = [['Fitness type','Population Size','Individual Size','Mutation Rate',
                    'Crossover Rate'],
                [fit, population_size, individual_size, mutation_rate, cross_over_rate]]
    print(tabulate(print_list))
    f = fitness()
    s = selection()
    p = population(population_size)
    
    for ind in p.pop:
        #print(ind.val)
        ind.fit = f.returnFitness(ind)


    #print_headers_list = [['Gen #', ' Max Fitness','Avg Fitness', '% Same']]
    gen = 0
    
    print('##############################################################')
    print('Generation','\t','Max Fit','\t','Average Fit','\t','% same','\t',)

    while gen < max_gens and not f.checkTerminate(p):
        '''print('##################')
        print('Initial Population')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''
        # Parent Selection
        p.parents = s.returnSelection(p)

        '''print('##################')
        print('After Parent Selection')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''
        # Mutation
        for ind in p.parents:
            ind.mutate(mutation_rate)
        
        '''print('##################')
        print('After Mutation')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''
        
        # Crossover
        
        # Mew , Lambda Survivor Selection
        # clears the population
        p.pop = []
        while len(p.pop) < p.pop_size:
            ind = random.choice(p.parents)
            r = random.random()
            if r <= cross_over_rate:
                ind2 = random.choice(p.parents)
                ind = ind.crossover(ind2)
            p.pop.append(ind)

        '''
        print('##################')
        print('After Crossover')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''

        # Calculates the fitness of the new population
        for ind in p.pop:
            #ind.val = child_pop[i]
            ind.fit = f.returnFitness(ind)
            #i += 1

        gen += 1
        m, a, per = p.popStats()
        if maxFit:
            if best_m < float(m) : best_m = float(m)
            #if best_a < a : best_a = a
            #if best_per < per : best_per = per
        else:
            if best_m > float(m) : best_m = float(m)
            #if best_a < a : best_a = a
            #if best_per < per : best_per = per

        print(gen,'\t\t',m,'\t',a,'\t',per,'%')
    #for i in p.pop:
    #    print(i.val)
    if gen == max_gens:
        print(f"Best fit {best_m}")
    return None

# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    args = parse_arguments()
    try:
        main(**vars(args))
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        exit(-1)