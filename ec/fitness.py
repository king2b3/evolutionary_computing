''' Holds the fitness structure.

    Later I want to modify this to take in the population and/or individual object, but not needed yet

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import abc
import math

class Fitness(abc.ABC):
    def __init__(self) -> None:
        ''' Abstract class that contains a fitness function
        '''
        self.fit_count = 0
    
    @abc.abstractmethod
    def checkTerminate(self, pop) -> bool:
        ''' Returns True if the termination conditions are met
        '''
        pass


class RosenbrockNDim(Fitness):
    ''' 𝑓(𝑥, 𝑦) = (𝑎 − 𝑥)^2 + 𝑏(𝑦 − 𝑥^2) where 𝑎 = 1 and 𝑏 = 100

        First half of the individual is x, second half is y.
        
        For an individual sized N, a fixed point splits is like this
          X = S(N/4,N/4)
    '''
    def translate(self, n, split=0) -> float:
        ''' Returns the float value from IEEE 745
        '''
        if split != 0:
            pass
        else:
            split = math.ceil(len(n)/2) - 1

        # determins the sign of the number
        if n[0]:
            sign = -1
        else:
            sign = 1

        # splits the list into the left and right sides of the float
        left = n[1:split]
        right = n[split:]

        # combines the left hand side into an int
        left = int(bin(int(''.join(map(str, left)), 2)), 2)
        
        # adds the right hand floating value to the left side
        new_right = 0
        temp = 0.5
        for m in right:
            if m:
                new_right += temp
            temp = temp / 2
        return (sign) * (left + new_right)

    def returnFitnessSGA(self, ind) -> float:
        # splits the individual into multiple variables
        sum_fit = 0
        for x in range(0,len(ind.val)-7,7):
            x_i = self.translate(ind.val[x:x+7])
            x_1 = self.translate(ind.val[x+7:x+14])
            if x_i > 5.11:
                x_i = 5.11
            elif x_i < -5.12:
                x_i = -5.12
            if x_1 > 5.11:
                x_1 = 5.11
            elif x_1 < -5.12:
                x_1 = -5.12
            sum_fit += 100*(x_1 - x_i**2)**2 + (x_i - 1)**2            
        # returns the rosenbrock value of the two variables
        self.fit_count += 1
        return sum_fit

    def returnFitnessES(self, ind) -> float:
        sum_fit = 0
        for x in range(len(ind.val[:-1])):
            x_1 = ind.val[x+1]
            x_i = ind.val[x]
            if x_i > 5.11:
                x_i = 5.11
            elif x_i < -5.12:
                x_i = -5.12
            if x_1 > 5.11:
                x_1 = 5.11
            elif x_1 < -5.12:
                x_1 = -5.12
            sum_fit += 100*(x_1 - x_i**2)**2 + (x_i - 1)**2 
        # return summed fitness
        self.fit_count += 1
        return sum_fit

    def checkTerminate(self, p) -> bool:
        # if the population is all 1,1 IE the fit of each individual is 0
        return 0 == min(i.fit for i in p.pop)
    
    def checkTerminateNDim(self, p) -> bool:
        for i in p.pop:
            if i.fit == 0:
                return True
        return False



# task 1
class Himmelblau(Fitness):
    def returnFitness(self, ind) -> float:
        '''Returns the fitness of an individual
        '''
        return ((ind.x**2 + ind.y - 11)**2 + (ind.x + ind.y**2 -7)**2)
    
    def checkTerminate(self, p) -> bool:
        '''Returns True if the termination conditions are met
        '''
        count = 0
        for ind in p.pop:
            self.fit_count += 1
            if ind.fit == 0.0:
                count+=1
        return count == p.pop_size


# the task 3 implementation which needs to convert he bit string into floats for the calculations
class HimmelblauTask3(Fitness):
    def translate(self, n, split=0) -> float:
        ''' Returns the float value from IEEE 745
        '''
        if split != 0:
            pass
        else:
            split = math.ceil(len(n)/2) - 1

        # determins the sign of the number
        if n[0]:
            sign = -1
        else:
            sign = 1

        # splits the list into the left and right sides of the float
        left = n[1:split]
        right = n[split:]

        # combines the left hand side into an int
        left = int(bin(int(''.join(map(str, left)), 2)), 2)
        
        # adds the right hand floating value to the left side
        new_right = 0
        temp = 0.5
        for m in right:
            if m:
                new_right += temp
            temp = temp / 2
        return (sign) * (left + new_right)   

    def returnFitness(self, ind) -> float:
        ''' Returns the fitness of an individual
        '''
        x = self.translate(ind.val[:int(ind.size/ind.num_of_variables)])
        y = self.translate(ind.val[int(ind.size/ind.num_of_variables):])
        # just used for plotting stats
        ind.x = x
        ind.y = y
        # increment number of fitness calcs 
        self.fit_count += 1
        return ((x**2 + y - 11)**2 + (x + y**2 -7)**2)
    
    def checkTerminate(self, p) -> bool:
        ''' Returns True if the termination conditions are met
        '''
        count = 0
        for ind in p.pop:
            self.fit_count += 1
            if ind.fit == 0.0:
                count+=1
        return count == p.pop_size


class MaxOnes(Fitness):
    ''' Goal is to have the genotype be all 1s
    '''
    def returnFitness(self, ind) -> float:
        ''' Sums the individual since its just a list of 0s and 1s. 
              Divides by the length of the individual.
        '''
        # sums the list, [1,1,1,1,0,0] would have sum 4 
        return sum(ind.val)/ind.size

    def checkTerminate(self, p) -> bool:
        ''' Creates a list of [1,1,1,...1] the size of the desired individual
              I should pass in the full population class so it can call the length, but here we are
            Sizes based off of first entry in the population, since all individuals are the same size
            If the number of individuals that are all [1,1,1...1] = the length of the pop, the we can exit
        '''
        count = 0
        for ind in p.pop:
            # [1]*4 would result in [1,1,1,1]
            if [1]*p.ind_size == ind.val:
                count += 1
        # if each individual is all 1s
        return count == p.pop_size


class RosenbrockFixed(Fitness):
    ''' 𝑓(𝑥, 𝑦) = (𝑎 − 𝑥)^2 + 𝑏(𝑦 − 𝑥^2) where 𝑎 = 1 and 𝑏 = 100

        First half of the individual is x, second half is y.
        
        For an individual sized N, a fixed point splits is like this
          X = S(N/4,N/4)
    '''
    def translate(self, n, split=0) -> float:
        ''' Returns the float value from IEEE 745
        '''
        if split != 0:
            pass
        else:
            split = math.ceil(len(n)/2) - 1

        # determins the sign of the number
        if n[0]:
            sign = -1
        else:
            sign = 1

        # splits the list into the left and right sides of the float
        left = n[1:split]
        right = n[split:]

        # combines the left hand side into an int
        left = int(bin(int(''.join(map(str, left)), 2)), 2)
        
        # adds the right hand floating value to the left side
        new_right = 0
        temp = 0.5
        for m in right:
            if m:
                new_right += temp
            temp = temp / 2
        return (sign) * (left + new_right)

    def returnFitness(self, individual, a=1, b=100) -> float:
        # splits the individual into multiple variables
        x = self.translate(individual.val[:individual.num_of_variables])
        y = self.translate(individual.val[individual.num_of_variables:])
        # returns the rosenbrock value of the two variables
        return abs((a-x)**2 + b*(y-x**2)**2)

    def checkTerminate(self, p) -> bool:
        # if the population is all 1,1 IE the fit of each individual is 0
        return 0 == min(i.fit for i in p.pop)


""" DISREGARD. Gave a high a high precision binary floating representation a try
      and it was NOT a good idea. The range IEEE 745 gave was way too large for
      this problem scope.

      Leaving the code here as a reference
"""

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
        return abs((a-x)**2 + b*(y-x**2)**2)

    def checkTerminate(self, p) -> bool:
        return 0 == min(i.fit for i in p.pop)
