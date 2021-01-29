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
    parser.add_argument('population_size', 
            help='Initial size of the population.')
    parser.add_argument('individual_size', 
            help='Size of the genome of each individual.')
    parser.add_argument('individual_split', 
            help='Number of variables in the individual genome.')
    parser.add_argument('fitness', 
            help='Pick the fitness function type. Options: rosenbrock, max_ones')
    parser.add_argument('-mg','--max_gens', default=2000,
            help='Maximum number of generations allowed')
    parser.add_argument('-cr','--cross_over_rate', default=0.5,
            help='Crossover rate. Options in range [0,1]')
    parser.add_argument('-mr','--mutation_rate', default=0.001,
            help='Mutation rate. Options in range [0,1]')
    parser.add_argument('-s','--selection', default='roulette',
            help='The type of selection function used. Options: random, roulette.')
    parser.add_argument('-k', default=1, 
            help='K-point crossover. Options in range [1:Genome Size - 1]')
    args = parser.parse_args(args=args)
    return args

def main(population_size, individual_size, individual_split, fitness, cross_over_rate
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
    from population import CGA 
    
    
    f = MaxOnes()
    s = RouletteWheelSelection()
    p = CGA(population_size, individual_size, individual_split, cross_over_rate)

    print(fitness, population_size, individual_size)
    gens = 0
    while gen < max_gens or f.checkTerminate(p.pop):
        for ind in p.pop:
            ind.fit = f.returnFitness(ind)
        
        p.pop = s.returnSelection(p.pop)

        for ind in p.pop:
            ind.mutate(mutation_rate, mutation_rate)
        
        child_pop = []
        i = 0
        while len(child_pop) < p.pop_size:
            r = random.random()
            if r <= cross_over_rate:
                ind2 = random.choice(p.pop)
                ind1, ind2 = pop[i].singlePointCrossover(ind2)
                child_pop.append(ind1)
                child_pop.append(ind2)
            else:
                child_pop.append(pop[i])
            i += 1
            if i >= p.pop_size:
                i = 0
                random.shuffle(p.pop)
        p.pop = child_pop.copy()
        gen += 1
        print(gen,max(p.pop, key=lambda i: i.fit), )
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