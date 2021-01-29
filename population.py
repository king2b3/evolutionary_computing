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
        for _ in range(self.pop_size):
            self.pop.append(BitString(ind_size,num_of_variables))
    
    def getMaxInd(self) -> float:
        return max(self.pop, key=lambda i: i.fit).fit
    
    def getAverageInd(self) -> float:
        total_fit = sum(i.fit for i in self.pop)
        return total_fit / self.pop_size
    
    def getNumSame(self) -> float:
        count = 0
        for ind in self.pop:
            if [1]*self.ind_size == ind.val:
                count += 1
        return count / self.pop_size    
    
    def popStats(self) -> list:
        return f"{self.getMaxInd():.4f}", \
                f"{self.getAverageInd():.4f}", \
                f"{self.getNumSame():.4f}"


def main():
    b = Population(10,4,2)
    print(b.pop)

if __name__ == "__main__":
    main()