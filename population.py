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
        self.generate(ind_size,num_of_variables)

    def generate(self, ind_size, num_of_variables) -> None:
        for _ in range(self.pop_size):
            self.pop.append(BitString(ind_size,num_of_variables))
    
    def getMaxInd(self) -> float:
        return max(self.pop, key=lambda i: i.fit)
    
    def getAverageInd(self) -> float:
        total_fit = sum(i.fit for i in self.pop)
        return total_fit / pop_size
    
    def getNumSame(self) -> float:
        pass
    
    def __str__(self) -> list:
        return [self.getMaxInd, self.getAverageInd, self.getNumSame]]


def main():
    b = CGA(10,4,2)
    print(b.pop)

if __name__ == "__main__":
    main()