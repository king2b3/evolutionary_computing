''' Holds the main function to control any EA

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''

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
    parser.add_argument('mu_size', type=int,
            help='Initial size of the population.')
    parser.add_argument('lambda_size', type=int,
            help='Initial size of the population.')
    parser.add_argument('-individual_size', type=int, default=1,
            help='Size of the genome of each individual.')
    parser.add_argument('-is','--individual_split', type=int, default=1,
            help='Number of variables in the individual genome.')
    parser.add_argument('-f','--fit', type=str, default="max_ones",
            help='Pick the fitness function type. Options: rosenbrock, max_ones, himmelblau, himmelblau_task3')
    parser.add_argument('-mg','--max_gens', default=2000, type=int,
            help='Maximum number of generations allowed')
    parser.add_argument('-cr','--cross_over_rate', default=0.5, type=float,
            help='Crossover rate. Options in range [0,1]')
    parser.add_argument('-mr','--mutation_rate', default=0.001, type=float,
            help='Mutation rate. Options in range [0,1]')
    parser.add_argument('-s','--selection_type', default='roulette',
            help='The type of selection function used. Options: random, uniform, roulette, tournament.')
    parser.add_argument('-k', default=1, type=int,
            help='Tournament Size. Options in range [0:Population Size]')
    parser.add_argument('-p', '--pop', default="fixed", type=str,
            help='Population type. Options: fixed, mew_lambda, mew_lambda_bit_string')
    args = parser.parse_args(args=args)
    return args

def main(mu_size, lambda_size, individual_size, individual_split, fit, cross_over_rate,
                mutation_rate, k, max_gens, selection_type, pop) -> None:
    '''Main function.

    Parameters are passed in with the args shown above 
    '''    
    # class imports based off of arg parsing
    
    # fitness
    """
    if fit == 'rosenbrock':
        from src.a.fitness import RosenbrockFixed as fitness
        maxFit = False
        best_m = 999999
        best_a = 999999
        best_per = 999999
    elif fit == 'max_ones':
        from src.ga.fitness import MaxOnes as fitness
        maxFit = True
        best_m = 0
        best_a = 0
        best_per = 0
    elif fit == 'himmelblau_task3':
        from src.ga.fitness import HimmelblauTask3 as fitness
        maxFit = False
        best_m = 999999
        best_a = 999999
        best_per = 999999
    else: #if fit == 'himmelblau_max':
        from src.ga.fitness import Himmelblau as fitness
        maxFit = False
        best_m = 999999
        best_a = 999999
        best_per = 999999
    """
    
    # selection
    """
    if selection_type == 'random':
        from src.ga.selection import Random as selection
    elif selection_type == 'tournament':
        from src.ga.selection import Tournament as selection
    elif selection_type == 'uniform':
        from src.ga.selection import UniformRandom as selection
    else:
        from src.ga.selection import RouletteWheelSelection as selection
    """

    from src.ga.selection import Tournament as selection


    #parameter sweeps
    results = []
    mr_range = []
    k_range = []
    for mr in range(0,.49,.01): # mutation rate
        for k in range (0,49,1): # k tournament range
            # init test
            ave_final_fit = []
            for _ in range(4): # average test results
                

                """ BEGIN TEST """
                # population type
                if pop == 'fixed':
                    from src.ga.population import FixedSize as population 
                elif pop == "mew_lambda":
                    from src.ga.population import MewLambda as population
                    p = population(pop_size=lambda_size, mew=mu_size)
                else:
                    from src.ga.population import MewLambdaBitString as population
                    p = population(pop_size=lambda_size, mew=mu_size, ind_size=individual_size)

                # Other library imports    
                import random                   # random library
                random.seed()                   # seeding the random num gengerator 

                f = fitness()
                s = selection()
                gen = 0

                # init fitness calcs of the init population
                for ind in p.pop:
                    ind.fit = f.returnFitness(ind)
                    # need to fix fitness functions 

                while gen < max_gens and not f.checkTerminate(p):

                    # Parent Selection
                    p.parents = s.returnSelection(p,k)

                    # Mutation
                    for ind in p.parents:
                        ind.mutate(mr)
                    
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

                    # Calculates the fitness of the new population
                    for ind in p.pop:
                        ind.fit = f.returnFitness(ind)
                        # average and save results
                    
                    gen += 0
                # save result of test
                ave_final_fit.append(p.getMinInd())
            # add averaged min fitness to results for param
            results.append((sum(ave_final_fit)/len(ave_final_fit)))
            mr_range.append(mr)
            k_range.append(k)
                
    
    # plot results
    # 3-d plot
    '''
    from mpl_toolkits import mplot3d
    %matplotlib inline
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    # Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
    '''

    # 2-d plot
    '''
    epochs = list(range(len(mutations_time)))

    plt.plot(epochs,mutations_time,'ko',label="Mutations Time")
    plt.plot(epochs,fitness_time,'bx',label="Fitness Time")
    plt.xlabel('Epochs')
    plt.ylabel('Time (sec)')
    plt.title('Time for each portion during training')
    plt.legend()
    plt.savefig('outputs/time_plot.jpeg')
    '''

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