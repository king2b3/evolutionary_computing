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

    def returnSelection(self, p) -> list:
        s = sum(i.fit for i in p.pop)
        if s == 0: # case when the population is all individuals of all 0s
            parent_pop = []
            for _ in range(p.pop_size):
                parent_pop.append(random.choice(p.pop))
        else: 
            for i in range(p.pop_size):
                if i == 0:
                    p.pop[i].fit_score = p.pop[i].fit / s
                else:
                    p.pop[i].fit_score = p.pop[i-1].fit_score + (p.pop[i].fit / s)
                #print(p.pop[i].val,p.pop[i].fit_score, p.pop[i].fit)
            parent_pop = []
            for n in range(p.pop_size):
                r = random.random()
                i = 0
                while r >= p.pop[i].fit_score:
                    i += 1
                parent_pop.append(p.pop[i])
        return parent_pop

class RouletteWheelSelectionMin(Selection):
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

    def returnSelection(self, p) -> list:
        s = sum(i.fit for i in p.pop)
        if s == 0: # case when the population is all individuals of all 0s
            parent_pop = []
            for _ in range(p.pop_size):
                parent_pop.append(random.choice(p.pop))
        else: 
            for i in range(p.pop_size):
                if i == 0:
                    p.pop[i].fit_score = p.pop[i].fit / s
                else:
                    p.pop[i].fit_score = p.pop[i-1].fit_score + (p.pop[i].fit / s)
                #print(p.pop[i].val,p.pop[i].fit_score, p.pop[i].fit)
            parent_pop = []
            for n in range(p.pop_size):
                r = random.random()
                i = 0
                while r >= 1 - abs(p.pop[i].fit_score):
                    i += 1
                parent_pop.append(p.pop[i])
        return parent_pop