''' Holds the individual structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''

import abc
import random
from numpy import random as npr
random.seed()

class Individual(abc.ABC):
    ''' Abstract structure for an individual.
          Initializes their fitness to 0.
    '''
    def __init__(self) -> None:
        self.fit = 0
        self.fit_score = 0

    @abc.abstractmethod
    def generate(self) -> None:
        ''' Method to generate a random individual
        '''
        pass

    @abc.abstractmethod
    def mutate(self, mut_rate) -> float:
        ''' Method to mutate the individual
        '''
        pass

    @abc.abstractmethod
    def crossover(self, ind2) -> list:
        ''' Method to crossover the individual with another individual
              Single point crossover
            
            Might make mutate and crossover into their own child classes of
              individual later. 
        '''
        pass

class BitString(Individual):
    ''' Bitstring representation genotype
          EX/ [1,0,1,1,1]
    '''
    def __init__(self, size, num_of_variables, val=None) -> None:
        self.size = size
        self.num_of_variables = num_of_variables
        # inits class with parent methods and variables
        super().__init__()
        if val:
            self.val = val
        else:
            self.generate()

    def generate(self) -> None:
        # sets value as a random list of 0s and 1s to the self.size
        self.val = random.choices([0,1],k=self.size)
    
    def mutate(self, mut_rate) -> None:
        # bitwise mutation rate
        for location in range(self.size):
            r = random.random()
            if r <= mut_rate:
                # 1 - 1 = 0 or 1 - 0 = 1. Flips the bits
                self.val[location] = 1 - self.val[location]

    def crossover(self, ind2) -> list:
        # picks random location in the bit string
        loc = random.randint(1,self.size-2)
        # creates temps of the two individuals
        temp1 = self.val.copy()
        temp2 = ind2.val.copy()
        # crossover at point loc
        ind1 = temp1[:loc] + temp2[loc:]
        return ind1
    

class FloatingPoint(Individual):
    def __init__(self, max_val=10, min_val=-10, x:int=None, y:int=None, ox=1, oy=1) -> None:
        super().__init__()

        self.sigma_x = ox
        self.sigma_y = oy
        if x and y:
            self.x = x
            self.y = y
        else:
            self.generate(max_val, min_val)
    
    def generate(self, max_val, min_val) -> None:
        """Sets random values for the X and Y floating point values

        Uniform chance to pick a value between min and max values
        """
        self.x = random.uniform(min_val, max_val)
        self.y = random.uniform(min_val, max_val)
 
    def mutate(self, mut_rate) -> None:
        """Gaussian Perturbation Mutation

        Each individual variable has a mut_rate chance to be mutated.

        Sigma_X and Sigma_Y are the standard deviation used for the X and Y variables' mutations
        Standard devitation of 1 is used when mutating Sigma_X and Sigma_Y. 
          Thinking about using themselves as standard deviation values, instead of using fixed values
        """
        for val, dev in [[self.x, self.sigma_x,], [self.y, self.sigma_y],
                [self.sigma_x, 1], [self.sigma_y, 1]]:
            r = random.random()
            if r <= mut_rate:
                val = npr.normal(val,dev)
        self.checkRange()
    
    def crossover(self, ind2) -> "Individual":
        """Performs an intermediate recombination of two individuals

        Returns:
        New individual, which is the child of the two parents
        """
        a = random.random()
        new_x = (self.x * a) + ((1-a) * ind2.x)
        new_y = (self.y * a) + ((1-a) * ind2.y)
        new_sigma_x = (self.sigma_x * a) + ((1-a) * ind2.sigma_x)
        new_sigma_y = (self.sigma_y * a) + ((1-a) * ind2.sigma_y)
        return FloatingPoint(x=new_x, y=new_y, ox=new_sigma_x, oy=new_sigma_y)
    
    def checkRange(self):
        """Checks if X or y are above 10 or below -10.
        If so, then the values are capped at the max ranges
        """
        if self.x > 10:
            self.x = 10
        elif self.x < -10:
            self.x = -10
        
        if self.y > 10:
            self.y = 10
        elif self.y < -10:
            self.y = -10


def main():
    # testing function
    b = BitString(10,2)
    c = BitString(10,2)
    print(b.val)
    print(c.val)
    for _ in range(1):
        b.val = b.singlePointCrossover(c)
        print(b.val)

if __name__ == "__main__":
    main()