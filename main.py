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
            help='K-point crossover. Options in range [1:Genome Size - 1]')
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
    
    # selection
    if selection_type == 'random':
        from src.ga.selection import Random as selection
    elif selection_type == 'tournament':
        from src.ga.selection import Tournament as selection
    elif selection_type == 'uniform':
        from src.ga.selection import UniformRandom as selection
    else:
        from src.ga.selection import RouletteWheelSelection as selection
    
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
    from tabulate import tabulate   # pretty plotting
    from os import system           # for clearing the terminal
    import random                   # random library
    random.seed()                   # seeding the random num gengerator

    # function to clear the terminal
    def clear():
        _ = system("clear")
    
    # clears the screen before the EA starts
    clear()    

    fit_count = []
    print_list = [['Fitness type','Mu Size','Lambda Size','Mutation STD','Mutation Rate',
                    'Crossover Rate'],
                [fit, mu_size, lambda_size, 1, mutation_rate, cross_over_rate]]
    print(tabulate(print_list))
    f = fitness()
    s = selection()

        
    for ind in p.pop:
        ind.fit = f.returnFitness(ind)

    gen = 0
    
    print('########################################################################################')
    print('Generation','\t','Candidate Evals','\t','Best Fit','\t','Average Fit','\t','% same','\t',)

    # I don't like to leave multiline comments in the code, but I left these since I found them to be helpful for debugging
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
            ind.fit = f.returnFitness(ind)

        gen += 1
        m, a, per = p.popStats()
        if maxFit:
            if best_m < float(m) : best_m = float(m)

        else:
            if best_m > float(m) : best_m = float(m)

        print(gen,'\t\t',f.fit_count,'\t\t\t',m,'\t',a,'\t',per,'%')

        # saves stats that will be plotted
        p.getPlotStats()
        fit_count.append(f.fit_count)

    if gen == max_gens:
        print(f"Best fit {best_m}")
    # wont print this is the EA terminated early, since every member of the population was the desired solution

    
    # Plots the 3 plots for task 2
    import matplotlib.pyplot as plt

    # Average Performance
    plt.figure()
    plt.plot(fit_count, p.average_performance,'bo',label="Average Performance")
    plt.xlabel('Candidate Evaluations')
    plt.ylabel('Average Performance')
    plt.title('Average Performance of Population for the Himmelblau Function')
    plt.savefig('average_performance.jpeg')

    # Euclidean Distance
    plt.figure()
    plt.plot(fit_count, p.euclidean,'ko',label="Euclidean Distance")
    plt.xlabel('Candidate Evaluations')
    plt.ylabel('Euclidean Distance')
    plt.title('Euclidean Distance of Population for the Himmelblau Function')
    plt.savefig('euclidean_performance.jpeg')

    # Best Performance
    plt.figure()
    plt.plot(fit_count, p.best_performance,'ro',label="Best Performance")
    plt.xlabel('Candidate Evaluations')
    plt.ylabel('Best Performance')
    plt.title('Best Performance of Population for the Himmelblau Function')
    plt.savefig('best_performance.jpeg')

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