''' Holds the individual structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''

import abc
import random
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
    def singlePointCrossover(self, ind2) -> list:
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
        super().__init__()
        if val:
            self.generate()
        else:
            self.val = val

    def generate(self) -> None:
        self.val = random.choices([0,1],k=self.size)
    
    def mutate(self, mut_rate) -> None:
        r = random.random()
        if r <= mut_rate:
            location = random.randint(0,self.size-1) 
            self.val[location] = 1 - self.val[location]

    def singlePointCrossover(self, ind2, ind1=self.val.copy()) -> list:
        loc = random.randint(0,len(self.val)-1)
        temp1 = self.val.copy()
        temp2 = ind2.copy()
        ind1 = temp1[:loc] + temp2[loc:]
        ind2 = temp2[:loc] + temp1[:loc]
        return ind1, ind2
    
def main():
    b = BitString(16,2)
    for _ in range(10):
        b.mutate()
        print(b.val)

if __name__ == "__main__":
    main()