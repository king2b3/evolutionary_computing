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
            self.val = val
        else:
            self.generate()

    def generate(self) -> None:
        self.val = random.choices([0,1],k=self.size)
    
    def mutate(self, mut_rate) -> None:
        for location in range(self.size):
            r = random.random()
            if r <= mut_rate:
                self.val[location] = 1 - self.val[location]

    def singlePointCrossover(self, ind2) -> list:
        loc = random.randint(1,self.size-2)
        #print(loc)
        ind1 = self.val.copy()
        temp1 = self.val.copy()
        temp2 = ind2.val.copy()
        ind1 = temp1[:loc] + temp2[loc:]
        #ind2 = temp2[:loc] + temp1[loc:]

        return ind1
        #return ind1, ind2
    
def main():
    b = BitString(10,2)
    c = BitString(10,2)
    print(b.val)
    print(c.val)
    for _ in range(1):
        b.val = b.singlePointCrossover(c)
        print(b.val)

if __name__ == "__main__":
    main()