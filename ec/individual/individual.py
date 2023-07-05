""" Holds the individual structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""

import random
from numpy import random as npr
random.seed()

from ec.engine.individual import Individual

class FloatingPoint(Individual):
    def __init__(self, n, max_val=5.11, min_val=-5.12, ox=1, oy=1) -> None:
        super().__init__()
        # standard deviations 
        self.val = []
        self.o = []
        # x and y values
        for _ in range(n):
            self.generate(max_val, min_val)
    
    def generate(self, max_val, min_val) -> None:
        """Sets random values for the X and Y floating point values

        Uniform chance to pick a value between min and max values
        """
        self.val.append(random.uniform(min_val, max_val))
        self.o.append(1)
 
    def mutate(self, mut_rate) -> None:
        """Gaussian Perturbation Mutation

        Each individual variable has a mut_rate chance to be mutated.

        Sigma_X and Sigma_Y are the standard deviation used for the X and Y variables' mutations
        Standard devitation of 1 is used when mutating Sigma_X and Sigma_Y. 
          Thinking about using themselves as standard deviation values, instead of using fixed values
        """
        for val, dev in zip(self.val, self.o):
            r = random.random()
            if r <= mut_rate:
                val = npr.normal(val,dev)
        self.checkRange()
    
    def crossover(self, ind2) -> None:
        """Performs an intermediate recombination of two individuals

        Returns:
        New individual, which is the child of the two parents
        """
        for i in range(len(self.val)):
            a = random.random()
            self.val[i] = (self.val[i] * a) + ((1-a) * ind2.val[i])
            self.o[i] = (self.o[i] * a) + ((1-a) * ind2.o[i])
    
    def checkRange(self):
        """Checks if X or y are above 10 or below -10.
        If so, then the values are capped at the max ranges
        """
        for x in self.val:
            if x > 5.11:
                x = 5.11
            elif x < -5.12:
                x = -5.12
        for o in self.o:
            o = abs(o)
    
    def __str__(self) -> str:
        return f"X :{self.x} Y:{self.y}"


class BitString(Individual):
    """ Bitstring representation genotype
          EX/ [1,0,1,1,1]
    """
    def __init__(self, size, mut_rate, val=None) -> None:
        self.size = size
        self.mut_rate = mut_rate
        # inits class with parent methods and variables
        super().__init__()
        if val:
            self.val = val
        else:
            self.generate()

    def generate(self) -> None:
        #TODO add docstring
        # sets value as a random list of 0s and 1s to the self.size
        self.val = random.choices([0,1],k=self.size)
    
    def mutate(self) -> None:
        #TODO add docstring
        # bitwise mutation rate
        for location in range(self.size):
            r = random.random()
            if r <= self.mut_rate:
                # 1 - 1 = 0 or 1 - 0 = 1. Flips the bits
                self.val[location] = 1 - self.val[location]

    def crossover(self, ind2) -> list:
        #TODO add docstring
        # picks random location in the bit string
        loc = random.randint(1,self.size-2)
        # creates temps of the two individuals
        temp1 = self.val.copy()
        temp2 = ind2.val.copy()
        # crossover at point loc
        ind1 = temp1[:loc] + temp2[loc:]
        return BitString(self.size, self.mut_rate, val=ind1)
    
    def __str__(self) -> str:
        return str(self.val)
