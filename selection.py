''' Holds the selection structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import random
random.seed()

class Selection(abc.ABC):
    def __init__(self) -> None:
        ''' Abstract class for the selection function
        '''
        pass

    @abstractmethod
    def returnSelection(self, pop) -> list:
        ''' Returns the parent population
        '''
        pass

class RouletteWheelSelection(Selection):
    ''' Roulette Wheel Selection Function

        The population is sorted based off of their fitness
        Each individual calculates their fitness proportional selection rate
          IE. Individual fitness / sum of fitnesses from the population
        
        A "wheel" is created where each individual has a chance of selection based off of
          their sorted fitness score.
        
        EX.
        Ind     Fit     Fit_Score   Wheel Range
          A      1         .1         [0., .1)
          B      4         .4         [.1, .5)
          C      5         .5         [.5, 1.]
    '''

    def returnSelection(self, pop) -> list:
        s = sum(i.fit for i in pop)
        pop = sorted(pop, key=lambda i: i.fit)
        for i in range(len(pop)):
            if i == 0:
                pop[i].fit_score = pop[i].fit / s
            else:
                pop[i].fit_score = pop[i].fit_score+ pop[i].fit / s
        parent_pop = []
        for _ in range(len(pop)):
            r = random.random()
            i = 0
            while r < pop[i].fit_score:
                i += 1
            parent_pop.append(pop[i])
        return parent_pop
