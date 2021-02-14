''' Holds the population structure.

    This one needs some more cleaning up for sure.
      Not sure if population class should be abstract or not, still thinking about it.
    
    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import abc
import random
random.seed()
from individual import BitString

class Population(object):
    ''' Canonical Genetic Algorithm
    '''
    def __init__(self, pop_size, ind_size, num_of_variables) -> None:
        self.pop_size = pop_size
        self.pop = []
        self.ind_size = ind_size
        self.generate(ind_size,num_of_variables)

    def generate(self, ind_size, num_of_variables) -> None:
        # creates pop_size individuals. Adds instances of the individuals to a list
        for _ in range(self.pop_size):
            self.pop.append(BitString(ind_size,num_of_variables))
    
    def getMaxInd(self) -> float:
        # max fitness in the current population
        return max(self.pop, key=lambda i: i.fit).fit
    
    def getAverageInd(self) -> float:
        # sums the fitness population so it can be averaged 
        return sum(i.fit for i in self.pop) / self.pop_size
    
    def getNumSame(self) -> float:
        ''' Create a dictionary where each key is every unique individual in the population

            The number of each individuals are counted.

            % unique = Total number with count > 2 / total individuals 
        '''
        # allows a default key in the dictionary with a default value of 0. 
        from collections import defaultdict 
        num_stats = defaultdict(lambda: 0)
        # counts each unique individuals 
        for ind in self.pop:
            num_stats[str(ind.val)] += 1
        # Sum the count of individuals whose count is higher than 1. Divide that by the pop size to get % of unique individuals
        return 100*sum(filter(lambda i: i > 1, num_stats.values())) / self.pop_size
            
        return count / self.pop_size    
    
    def popStats(self) -> list:
        # printed stats
        return f"{self.getMaxInd():.4f}", \
                f"{self.getAverageInd():.4f}", \
                f"{self.getNumSame():.4f}"


def main():
    # testing function
    b = Population(10,4,2)
    print(b.pop)

if __name__ == "__main__":
    main()