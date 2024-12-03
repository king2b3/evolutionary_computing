""" Holds the base population structure.

    This one needs some more cleaning up for sure.
      Not sure if population class should be abstract or not, still thinking
      about it.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""
import abc

class Population(abc.ABC):
    """Base abstract class to create a population of individuals
    """
    def __init__(self, population_size) -> None:
        self.population = None
        self.population_size = population_size

    def get_max_ind(self) -> float:
        """Returns the max fitness in the current population
        """
        return max(self.population, key=lambda i: i.fitness).fitness

    def get_min_ind(self) -> float:
        """Returns the max fitness in the current population
        """
        return min(self.population, key=lambda i: i.fitness).fitness

    def get_average_ind(self) -> float:
        """Returns the average fitness of hte population
        """
        return sum(i.fitness for i in self.population) / self.population_size

    @abc.abstractmethod
    def get_num_same(self) -> float:
        """Returns the number of unique individuals in the population

        Dependant on the individual type
        """

    def pop_stats(self) -> list:
        """Prints out the stats of a population"""
        return f"Max fitness: {self.get_max_ind():.4f}", \
               f"Average fitness: {self.get_average_ind():.4f}", \
               f"Minnimum Fitness: {self.get_min_ind():.4f}", \
               f"Percent Unique: {self.get_num_same():.2f}%"
