''' Holds the fitness structure.

    Later I want to modify this to take in the population and/or individual object, but not needed yet

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
class Fitness(abc.ABC):
    def __init__(self) -> None:
        ''' Abstract class that contains a fitness function
        '''
        None

    @abc.abstractmethod
    def returnFitness(self, ind) -> float:
        ''' Returns the fitness of an individual
        '''
        pass
    
    @abc.abstractmethod
    def checkTerminate(self, pop) -> bool:
        ''' Returns True if the termination conditions are met
        '''
        pass

class MaxOnes(Fitness):
    ''' Goal is to have the genotype be all 1s
    '''
    def returnFitness(self, ind) -> float:
        ''' Sums the individual since its just a list of 0s and 1s. 
              Divides by the length of the individual.
        '''
        return sum(ind.val)/ind.size

    def checkTerminate(self, pop) -> bool:
        ''' Creates a list of [1,1,1,...1] the size of the desired individual
              I should pass in the full population class so it can call the length, but here we are
            Sizes based off of first entry in the population, since all individuals are the same size
            If the number of individuals that are all [1,1,1...1] = the length of the pop, the we can exit
        '''
        return pop.count(random.choices([1],k=len(pop[0]))) == len(pop)

class Rosenbrock(Fitness):

    def returnFitness(self, individual) -> float:
        pass
    
    def checkTerminate(self, pop) -> bool:
        pass