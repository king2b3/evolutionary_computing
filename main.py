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
    #parser.add_argument('mu_size', type=int,
    #        help='Initial size of the population.')
    #parser.add_argument('lambda_size', type=int,
    #        help='Initial size of the population.')
    #parser.add_argument('-individual_size', type=int, default=1,
    #        help='Size of the genome of each individual.')
    #parser.add_argument('-is','--individual_split', type=int, default=1,
    #        help='Number of variables in the individual genome.')
    #parser.add_argument('-f','--fit', type=str, default="max_ones",
    #        help='Pick the fitness function type. Options: rosenbrock, max_ones, himmelblau, himmelblau_task3')
    #parser.add_argument('-mg','--max_gens', default=2000, type=int,
    #        help='Maximum number of generations allowed')
    #parser.add_argument('-cr','--cross_over_rate', default=0.5, type=float,
    #        help='Crossover rate. Options in range [0,1]')
    #parser.add_argument('-mr','--mutation_rate', default=0.001, type=float,
    #        help='Mutation rate. Options in range [0,1]')
    #parser.add_argument('-s','--selection_type', default='roulette',
    #        help='The type of selection function used. Options: random, uniform, roulette, tournament.')
    #parser.add_argument('-k', default=1, type=int,
    #        help='Tournament Size. Options in range [0:Population Size]')
    #parser.add_argument('-p', '--pop', default="fixed", type=str,
    #        help='Population type. Options: fixed, mew_lambda, mew_lambda_bit_string')
    args = parser.parse_args(args=args)
    return args

#def main(mu_size, lambda_size, individual_size, individual_split, fit, cross_over_rate,
#                mutation_rate, k, max_gens, selection_type, pop) -> None:
def main() -> None:
    '''Main function.

    Parameters are passed in with the args shown above 
    '''    
    from src.ga.selection import Tournament as selection
    from src.ga.fitness import RosenbrockNDim as fitness

    #parameter sweeps
    mr_range = []
    k_range = []
    max_gens = 1000
    cross_over_rate = 0.5

    """ SGA """
    print('########################')
    print('SGA Parameter Test')
    print('########################')
    sga_results = []
    for mr in range(1,20,1): # mutation rate
        mr = mr*.01
        for k in range (1,20,1): # k tournament range
            # init test
            ave_final_fit = []
            best_fit = 99999
            print(f"Mutation Rate {mr} and tournament size {k}")
            for _ in range(1): # average test results

                """ BEGIN TEST """
                # population type
                from src.ga.population import FixedSize as population 
                p = population(100,4)

                # Other library imports    
                import random                   # random library
                random.seed()                   # seeding the random num gengerator 

                f = fitness()
                s = selection()
                gen = 0

                # init fitness calcs of the init population
                for ind in p.pop:
                    ind.fit = f.returnFitnessSGA(ind)
                    # need to fix fitness functions 
                while gen < max_gens and not f.checkTerminate(p):
                    #print(gen)

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
                        ind.fit = f.returnFitnessSGA(ind)
                        # average and save results
                    
                    gen += 1
                # save result of test
                ave_final_fit.append(p.getMinInd())
            # add averaged min fitness to results for param
            temp = sum(ave_final_fit)/len(ave_final_fit)
            sga_results.append((temp))
            if temp < best_fit:
                best_fit = temp
                best_mr_sga = mr
                best_k_sga = k
            mr_range.append(mr)
            k_range.append(k)
    # find and save best mr and k combo from SGA tests

    """ ES """
    print('########################')
    print('ES Parameter Test')
    print('########################')
    es_results = []
    for mr in range(1,20,1): # mutation rate
        mr = mr*.01
        for k in range (1,20,1): # k tournament range
            # init test
            ave_final_fit = []
            best_fit = 99999
            print(f"Mutation Rate {mr} and tournament size {k}")
            for _ in range(1): # average test results
                
                """ BEGIN TEST """
                # population type
                from src.ga.population import MewLambda as population
                p = population(pop_size=100, mew=15, n=4)

                # Other library imports    
                import random                   # random library
                random.seed()                   # seeding the random num gengerator 

                f = fitness()
                s = selection()
                gen = 0

                # init fitness calcs of the init population
                for ind in p.pop:
                    ind.fit = f.returnFitnessES(ind)
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
                            ind.crossover(ind2)
                        p.pop.append(ind)

                    # Calculates the fitness of the new population
                    for ind in p.pop:
                        ind.fit = f.returnFitnessES(ind)
                        # average and save results

                    gen += 1
                # save result of test
                ave_final_fit.append(p.getMinInd())
            # add averaged min fitness to results for param
            temp = sum(ave_final_fit)/len(ave_final_fit)
            es_results.append((temp))
            if temp < best_fit:
                best_fit = temp
                best_mr_es = mr
                best_k_es = k
    # find and save best mr and k combo from ES tests
    
    print(f"SGA: best mutation rate {best_mr_sga} with {best_k_sga} tournament size")
    print(f"ES: best mutation rate {best_mr_es} with {best_k_es} tournament size")

    #################################################

    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    X, Y = np.meshgrid(mr_range, k_range)
    Z = np.array([sga_results])

    ax.plot_wireframe(X, Y, Z, color='green')
    ax.set_xlabel('Mutation Rate (mr)')
    ax.set_ylabel('Tournament Size (k)')
    ax.set_zlabel('Fitness')
    ax.set_title("Standard Genetic Algorithm against 4-D Rosenbrock")

    fig.savefig('outputs/sga_3d.jpeg')

    #################################################

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    X, Y = np.meshgrid(mr_range, k_range)
    Z = np.array([es_results])

    ax.plot_wireframe(X, Y, Z, color='green')
    ax.set_xlabel('Mutation Rate (mr)')
    ax.set_ylabel('Tournament Size (k)')
    ax.set_zlabel('Fitness')
    ax.set_title("Evolutionary Strategy against 4-D Rosenbrock")

    fig.savefig('outputs/es_3d.jpeg')

    #################################################

    best_k_es = 5
    best_k_sga = 5
    best_mr_es = 0.1
    best_mr_sga = 0.1
    max_gens = 4000

    """ SGA """
    print('########################')
    print('SGA Dimensions Test')
    print('########################')
    performance_sga = []
    for n in range(2,11): # mutation rate
        ave_final_fit = []
        print(f"Dimensions {n}")
        for _ in range(1): # average test results
            

            """ BEGIN TEST """
            # population type
            from src.ga.population import FixedSize as population 
            p = population(100,n)

            # Other library imports    
            import random                   # random library
            random.seed()                   # seeding the random num gengerator 

            f = fitness()
            s = selection()
            gen = 0

            # init fitness calcs of the init population
            for ind in p.pop:
                ind.fit = f.returnFitnessSGA(ind)
                # need to fix fitness functions 

            while gen < max_gens and not f.checkTerminateNDim(p):

                # Parent Selection
                p.parents = s.returnSelection(p,best_k_sga)

                # Mutation
                for ind in p.parents:
                    ind.mutate(best_mr_sga)
                
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
                    ind.fit = f.returnFitnessSGA(ind)
                    # average and save results
                
                gen += 1
            # save result of test
            ave_final_fit.append(f.fit_count)
        # add averaged min fitness to results for param
        performance_sga.append(sum(ave_final_fit)/len(ave_final_fit))

    """ ES """
    print('########################')
    print('ES Dimensions Test')
    print('########################')
    performance_es = []
    for n in range(2,11): # mutation rate
        ave_final_fit = []
        print(f"Dimensions {n}")
        for _ in range(1): # average test results
            

            """ BEGIN TEST """
            # population type
            from src.ga.population import MewLambda as population
            p = population(pop_size=100, mew=15, n=4)

            # Other library imports    
            import random                   # random library
            random.seed()                   # seeding the random num gengerator 

            f = fitness()
            f.fit_count = 0
            s = selection()
            gen = 0

            # init fitness calcs of the init population
            for ind in p.pop:
                ind.fit = f.returnFitnessES(ind)
                # need to fix fitness functions 

            while gen < max_gens and not f.checkTerminateNDim(p):

                # Parent Selection
                p.parents = s.returnSelection(p,best_k_es)

                # Mutation
                for ind in p.parents:
                    ind.mutate(best_mr_es)
                
                # Crossover
                
                # Mew , Lambda Survivor Selection
                # clears the population
                p.pop = []
                while len(p.pop) < p.pop_size:
                    ind = random.choice(p.parents)
                    r = random.random()
                    if r <= cross_over_rate:
                        ind2 = random.choice(p.parents)
                        ind.crossover(ind2)
                    p.pop.append(ind)

                # Calculates the fitness of the new population
                for ind in p.pop:
                    ind.fit = f.returnFitnessES(ind)
                    # average and save results
                
                gen += 1
            # save result of test
            ave_final_fit.append(f.fit_count)
        # add averaged min fitness to results for param
        performance_es.append(sum(ave_final_fit)/len(ave_final_fit))

    import matplotlib.pyplot as plt
    plt.figure()
    dims = [2,3,4,5,6,7,8,9,10]
    #dims = [2,3]
    plt.plot(dims,performance_es,'k*-',label="ES")
    plt.plot(dims,performance_sga,'b*-',label="SGA")
    plt.xlabel('Dimensions of Rosenbrock')
    plt.ylabel('Fitness Evaluations to a Solution')
    plt.title('Performance of the Configurations in Higher Dimensions')
    plt.legend()
    plt.savefig('outputs/time_plot.jpeg')


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