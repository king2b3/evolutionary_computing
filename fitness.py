''' Holds the fitness structure.

    Later I want to modify this to take in the population and/or individual object, but not needed yet

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import abc
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

    def checkTerminate(self, p) -> bool:
        ''' Creates a list of [1,1,1,...1] the size of the desired individual
              I should pass in the full population class so it can call the length, but here we are
            Sizes based off of first entry in the population, since all individuals are the same size
            If the number of individuals that are all [1,1,1...1] = the length of the pop, the we can exit
        '''
        count = 0
        for ind in p.pop:
            if [1]*p.ind_size == ind.val:
                count += 1
        return count == p.pop_size
        #return pop.count(random.choices([1],k=len(pop[0]))) == len(pop)

class RosenbrockIEEE(Fitness):
    ''' 𝑓(𝑥, 𝑦) = (𝑎 − 𝑥)^2 + 𝑏(𝑦 − 𝑥^2) where 𝑎 = 1 and 𝑏 = 100

        First half of the individual is x, second half is y
        IEEE 745. 32 bits for each number. Individual is 64 bits long
    '''

    def translate(self, n) -> float:
        ''' Returns the float value from IEEE 745
        '''
        if n[0]:
            sign = -1
        else:
            sign = 1
        exponent = n[1:9]
        mantissa = n[9:]

        exponent = int(bin(int(''.join(map(str, exponent)), 2)), 2)
        new_mantissa = 1
        temp = 0.5
        for m in mantissa:
            if m:
                new_mantissa += temp
            temp = temp / 2
        return (sign) * (new_mantissa) * 2**(exponent-127)

    def returnFitness(self, individual, a=1, b=100) -> float:
        x = self.translate(individual.val[:32])
        y = self.translate(individual.val[32:])
        return (a-x)**2 + b*(y-x**2)

    def checkTerminate(self, p) -> bool:
        return 0 == min(i.fit for i in p.pop)


class RosenbrockFixed(Fitness):
    ''' 𝑓(𝑥, 𝑦) = (𝑎 − 𝑥)^2 + 𝑏(𝑦 − 𝑥^2) where 𝑎 = 1 and 𝑏 = 100

        First half of the individual is x, second half is y.
        
        Option 2:
            For an individual sized N, a fixed point splits is like this
              X = S(N/4,N/4)
    '''
    def translate(self, n, split=4) -> float:
        ''' Returns the float value from IEEE 745
        '''
        
        if n[0]:
            sign = -1
        else:
            sign = 1
        left = n[1:split]
        right = n[split:]

        left = int(bin(int(''.join(map(str, left)), 2)), 2)
        new_right = 0
        temp = 0.5
        for m in right:
            if m:
                new_right += temp
            temp = temp / 2
        return (sign) * (left + new_right)

    def returnFitness(self, individual, a=1, b=100) -> float:
        x = self.translate(individual.val[:5])
        y = self.translate(individual.val[5:])
        return abs((a-x)**2 + b*(y-x**2))

    def checkTerminate(self, p) -> bool:
        return 0 == min(i.fit for i in p.pop)