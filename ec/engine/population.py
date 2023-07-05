""" Holds the base population structure.

    This one needs some more cleaning up for sure.
      Not sure if population class should be abstract or not, still thinking about it.
    
    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""
import abc

class Population(abc.ABC):
    def __init__(self, population_size) -> None:
        self.population = None
        self.population_size = population_size
        ...

    def getMaxInd(self) -> float:
        """Returns the max fitness in the current population
        """
        return max(self.population, key=lambda i: i.fitness).fitness

    def getMinInd(self) -> float:
        """Returns the max fitness in the current population
        """
        return min(self.population, key=lambda i: i.fitness).fitness

    def getAverageInd(self) -> float:
        """Returns the average fitness of hte population 
        """
        return sum(i.fitness for i in self.population) / self.population_size

    @abc.abstractmethod
    def getNumSame(self) -> float:
        """Returns the number of unique individuals in the population

        Dependant on the individual type
        """
        ...

    def popStats(self) -> list:
        """Prints out the stats of a population
        """
        return f"Max fitness: {self.getMaxInd():.4f}", \
               f"Average fitness: {self.getAverageInd():.4f}", \
               f"Minnimum Fitness: {self.getMinInd():.4f}", \
               f"Percent Unique: {self.getNumSame():.2f}%"
