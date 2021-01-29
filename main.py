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
    parser.add_argument('individual_split', type=int,
            help='Number of variables in the individual genome.')
    parser.add_argument('-f','--fit', type=str, default="max_ones",
            help='Pick the fitness function type. Options: rosenbrock, max_ones')
    parser.add_argument('-mg','--max_gens', default=2000, type=int,
            help='Maximum number of generations allowed')
    parser.add_argument('-cr','--cross_over_rate', default=0.5, type=float,
            help='Crossover rate. Options in range [0,1]')
    parser.add_argument('-mr','--mutation_rate', default=0.001, type=float,
            help='Mutation rate. Options in range [0,1]')
    parser.add_argument('-s','--selection', default='roulette',
            help='The type of selection function used. Options: random, roulette.')
    parser.add_argument('-k', default=1, type=int,
            help='K-point crossover. Options in range [1:Genome Size - 1]')
    args = parser.parse_args(args=args)
    return args

def main(population_size, individual_size, individual_split, fit, cross_over_rate,
                mutation_rate, selection, k, max_gens) -> None:
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
    selection: str:
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
    from timer import Timer
    from fitness import MaxOnes
    from selection import RouletteWheelSelection 
    from population import Population 
    from tabulate import tabulate
    from individual import Individual
    from os import system
    import random
    random.seed()
    
    def clear():
        _ = system("clear")
    
    f = MaxOnes()
    s = RouletteWheelSelection()
    p = Population(population_size, individual_size, individual_split)
    
    for ind in p.pop:
        ind.fit = f.returnFitness(ind)


    print_headers_list = [['Gen #', ' Max Fitness','Avg Fitness', '% Same']]
    gen = 0
    clear()
    
    print_list = [['Fitness type','Population Size','Individual Size','Mutation Rate',
                    'Crossover Rate'],
                [fit, population_size, individual_size, mutation_rate, cross_over_rate]]
    print(tabulate(print_list))
    print('##############################################################')
    print('Generation','\t','Max Fit','\t','Average Fit','\t','% same','\t',)
    
    while gen < max_gens and not f.checkTerminate(p):
        '''print('##################')
        print('Initial Population')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''
        # Selection
        p.pop = s.returnSelection(p)

        '''print('##################')
        print('After Selection')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''
        # Mutation
        for ind in p.pop:
            ind.mutate(mutation_rate)
        
        '''print('##################')
        print('After Mutation')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''
        
        # Crossover
        child_pop = []
        for ind in p.pop:
            r = random.random()
            if r <= cross_over_rate:
                ind2 = random.choice(p.pop)
                ind1, ind2 = ind.singlePointCrossover(ind2)
                child_pop.append(ind1)
                #child_pop.append(ind2)
            else:
                child_pop.append(ind.val)
        #random.shuffle(child_pop)
        i = 0
        for ind in p.pop:
            ind.val = child_pop[i]
            ind.fit = f.returnFitness(ind)
            i += 1
        
        '''print('##################')
        print('After Crossover')
        for ind in p.pop:
            print(ind.val)
        print('##################')
        '''       
        gen += 1
        m, a, per = p.popStats()
        print(gen,'\t\t',m,'\t',a,'\t',per,'\t',)
    for i in p.pop:
        print(i.val)
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