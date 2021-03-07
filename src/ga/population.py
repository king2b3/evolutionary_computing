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
from ga.individual import FloatingPoint


class Population(abc.ABC):
    def __init__(self, pop_size) -> None:
        ...

    @abc.abstractmethod
    def generate(self) -> None:
        """Generates a random population of size pop_size
        """
        ...
    
    def getMaxInd(self) -> float:
        """Returns the max fitness in the current population
        """
        return max(self.pop, key=lambda i: i.fit).fit
    
    def getAverageInd(self) -> float:
        """Returns the average fitness of hte population 
        """
        return sum(i.fit for i in self.pop) / self.pop_size
    
    @abc.abstractmethod
    def getNumSame(self) -> float:
        """Returns the number of unique individuals in the population

        Dependant on the individual type
        """
        ...
    
    def popStats(self) -> list:
        """Prints out the stats of a population
        """
        return f"{self.getMaxInd():.4f}", \
                f"{self.getAverageInd():.4f}", \
                f"{self.getNumSame():.4f}"


class MewLambda(Population):
    ''' Supports Mew Lambda populations
    '''
    def __init__(self, pop_size=100, mew=15) -> None:
        self.pop_size = pop_size
        self.mew = mew
        self.pop = []
        self.parents = []
        self.generate()

    def generate(self) -> None:
        # creates pop_size individuals. Adds instances of the individuals to a list
        for _ in range(self.pop_size):
            self.pop.append(FloatingPoint())
        
    def getNumSame(self) -> float:
        """Create a dictionary where each key is every unique individual in the population
        The number of each individuals are counted.
        % unique = Total number with count > 2 / total individuals 

        Returns
            % unique individuals in the population
        """
        # allows a default key in the dictionary with a default value of 0. 
        from collections import defaultdict 
        num_stats = defaultdict(lambda: 0)
        # counts each unique individuals 
        for ind in self.pop:
            num_stats["{:.5f}".format(ind.x + ind.y)] += 1
        # Sum the count of individuals whose count is higher than 1. Divide that by the pop size to get % of unique individuals
        return 100*sum(filter(lambda i: i > 1, num_stats.values())) / self.pop_size
            
        return count / self.pop_size 


class FixedSize(Population):
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
        
    def getNumSame(self) -> float:
        """Create a dictionary where each key is every unique individual in the population
        The number of each individuals are counted.
        % unique = Total number with count > 2 / total individuals 

        Returns
            % unique individuals in the population
        """
        # allows a default key in the dictionary with a default value of 0. 
        from collections import defaultdict 
        num_stats = defaultdict(lambda: 0)
        # counts each unique individuals 
        for ind in self.pop:
            num_stats[str(ind.val)] += 1
        # Sum the count of individuals whose count is higher than 1. Divide that by the pop size to get % of unique individuals
        return 100*sum(filter(lambda i: i > 1, num_stats.values())) / self.pop_size
            
        return count / self.pop_size  
    


def main():
    # testing function
    b = Population(10,4,2)
    print(b.pop)

if __name__ == "__main__":
    main()