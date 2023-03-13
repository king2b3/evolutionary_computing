''' Holds the selection structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import random
random.seed()
from ec.engine.selection import Selection


class UniformRandom(Selection):
    """Uniform Random Selection for parents

    Each individual has the same chance to be selected
    """
    def __init__(self, selection_size):
        """Creation of the Uniform Random selection function
        """
        super().__init__(selection_size)

    def __call__(self, p) -> list:
        new_pop = []
        for _ in range(self.sel_size):
            new_pop.append(random.choice(p))
        return new_pop

class RouletteWheelSelection(Selection):
    ''' Roulette Wheel Selection Function

        The population is sorted based off of their fitness
        Each individual calculates their fitness proportional selection rate
          IE. Individual fitness / sum of fitnesses from the population
        
        A "wheel" is created where each individual has a chance of selection based 
        off of their sorted fitness score.
        
        EX.
        Ind     Fit     Fit_Score   Wheel Range
          A      1         .1         [0., .1)
          B      4         .4         [.1, .5)
          C      5         .5         [.5, 1.]
    '''

    def __init__(self, selection_size):
        """Creation of the Roulette Wheel selection function
        """
        super().__init__(selection_size)

    def __call__(self, p) -> list:
        s = sum(i.fitness for i in p.population)
        p.population = sorted((ind for ind in p.population), key=lambda ind: ind.fitness)
        if s == 0: 
            # case when the population is all individuals of all 0s
            # no need to run the function, since they are all the same
            return p.population
        else: 
            # determines the proportional fitness 
            for i in range(p.population_size):
                if i == 0:
                    p.population[i].fit_score = p.population[i].fitness / s
                else:
                    p.population[i].fit_score = p.population[i-1].fit_score + (p.population[i].fitness / s)
            parent_pop = []
            # runs the roulette wheel
            for n in range(self.sel_size):
                r = random.random()
                i = 0
                while r >= p.population[i].fit_score:
                    i += 1
                parent_pop.append(p.population[i])
        return parent_pop

class Tournament(Selection):
    ''' Tournament selection type. K individuals are selected, and face off in a 
          tournament where the best individual is then passed onto the parent 
          population. 

        The K value can be changed to allow for larger tournaments.

        The tournament is just selecting which individual has the highest overall 
          fitness, there isn't a direct head-to-head bracket style match up that 
          one would associate with a competitive tournament.
    '''
    def __call__(self, population, k=2) -> list:
        parent_pop = []
        while len(parent_pop) < population.population_size:
            tournament = random.choices(population.population,k=4)
            parent_pop.append(max(tournament, key=lambda i: i.fitness))
        return parent_pop
    
class Random(Selection):
    ''' Returns a parent population all selected randomly with replacement from 
          the current population
    '''
    def __call__(self, population) -> list:
        parent_pop = []
        while len(parent_pop) < population.population_size:
            parent_pop.append(random.choice(population.population))
        return parent_pop