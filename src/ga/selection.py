''' Holds the selection structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import abc
import random
random.seed()

class Selection(abc.ABC):
    def __init__(self) -> None:
        ''' Abstract class for the selection function
        '''
        pass

    @abc.abstractmethod
    def returnSelection(self, pop) -> list:
        ''' Returns the parent population
        '''
        pass


class UniformRandom(Selection):
    """Uniform Random Selection for parents

    Each individual has the same chance to be selected
    """
    def returnSelection(self, p) -> list:
        p.parents = []
        for _ in range(p.mew):
            p.parents.append(random.choice(p.pop))
        return p.parents

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

    def returnSelection(self, p) -> list:
        s = sum(i.fit for i in p.pop)
        p.pop = sorted((ind for ind in p.pop), key=lambda ind: ind.fit)
        if s == 0: 
            # case when the population is all individuals of all 0s
            # no need to run the function, since they are all the same
            return p.pop
        else: 
            # determines the proportional fitness 
            for i in range(p.pop_size):
                if i == 0:
                    p.pop[i].fit_score = p.pop[i].fit / s
                else:
                    p.pop[i].fit_score = p.pop[i-1].fit_score + (p.pop[i].fit / s)
            parent_pop = []
            # runs the roulette wheel
            for n in range(p.pop_size):
                r = random.random()
                i = 0
                while r >= p.pop[i].fit_score:
                    i += 1
                parent_pop.append(p.pop[i])
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
    def returnSelection(self, population, k=2) -> list:
        parent_pop = []
        while len(parent_pop) < population.pop_size:
            tournament = random.choices(population.pop,k=2)
            parent_pop.append(max(population.pop, key=lambda i: i.fit))
        return parent_pop
    
class Random(Selection):
    ''' Returns a parent population all selected randomly with replacement from 
          the current population
    '''
    def returnSelection(self, population) -> list:
        parent_pop = []
        while len(parent_pop) < population.pop_size:
            parent_pop.append(random.choice(population.pop))
        return parent_pop