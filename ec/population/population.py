"""Holds the population structure.

   This one needs some more cleaning up for sure.
     Not sure if population class should be abstract or not, still thinking about it.

   Created on: 1-27-2021
   Version: Python 3.8.5
   Created by: Bayley King (https://github.com/king2b3)
"""
import random
random.seed()


from ec.individual.individual import FloatingPoint
from ec.individual.individual import BitString
from ec.engine.population import Population

from ec.fitness import Fitness


class MewLambda(Population):
    """Supports Mew Lambda populations for Task 1 with Floating Point
    individuals"""
    def __init__(self, pop_size=100, mew=15, n=4) -> None:
        self.population_size = pop_size
        self.mew = mew
        self.population = []
        self.parents = []
        self.n = n
        self.generate()

        # plotting lists
        self.average_performance = []
        self.best_performance = []
        self.euclidean = []

    def get_plot_stats(self):
        """Saves the current stats that will be plotted at the end of the EA"""
        self.average_performance.append(self.getAverageInd())
        self.best_performance.append(self.getMinInd())
        max_dist = 0
        # dumb but easy way to find max euclidean distance between two points
        # in the population
        for ind1 in self.population:
            for ind2 in self.population:
                dist = ((ind1.x - ind2.x)**2 + (ind1.y - ind2.y)**2)**.5
                if dist > max_dist:
                    max_dist = dist
        self.euclidean.append(max_dist)

    def pop_stats(self) -> list:
        """Prints out the stats of a population"""
        return f"{self.getMinInd():.4f}", \
                f"{self.getAverageInd():.4f}", \
                f"{self.getNumSame():.4f}"

    def generate(self) -> None:
        """creates individuals. Adds instances of the individuals to a list"""
        for _ in range(self.population_size):
            self.population.append(FloatingPoint(self.n))

    def getNumSame(self) -> float:
        """Create a dictionary where each key is every unique individual in the
        population.
        The number of each individuals are counted.
        % unique = Total number with count > 2 / total individuals

        Returns
            % unique individuals in the population
        """
        # allows a default key in the dictionary with a default value of 0.
        from collections import defaultdict
        num_stats = defaultdict(lambda: 0)
        # counts each unique individuals 
        for ind in self.population:
            num_stats["{:.5f}".format(ind.x + ind.y)] += 1
        # Sum the count of individuals whose count is higher than 1.
        # Divide that by the pop size to get % of unique individuals
        return 100*sum(filter(lambda i: i > 1, num_stats.values())) \
                / self.population_size

# same as above but for task 3
class MewLambdaBitString(Population):
    """Supports Mew Lambda populations"""
    def __init__(self, ind_size=16, pop_size=100, mew=15) -> None:
        self.population_size = pop_size
        self.mew = mew
        self.population = []
        self.parents = []
        self.ind_size = ind_size
        self.generate()

        # plotting lists
        self.average_performance = []
        self.best_performance = []
        self.euclidean = []

    def get_plot_stats(self):
        self.average_performance.append(self.getAverageInd())
        self.best_performance.append(self.getMinInd())
        max_dist = 0
        # dumb but easy way to find max euclidean distance between two points
        # in the population
        for ind1 in self.population:
            for ind2 in self.population:
                dist = ((ind1.x - ind2.x)**2 + (ind1.y - ind2.y)**2)**.5
                if dist > max_dist:
                    max_dist = dist
        self.euclidean.append(max_dist)

    def pop_stats(self) -> list:
        """Prints out the stats of a population"""
        return f"{self.getMinInd():.4f}", \
                f"{self.getAverageInd():.4f}", \
                f"{self.getNumSame():.4f}"

    def generate(self) -> None:
        """Creates the population"""
        # creates pop_size individuals. Adds instances of the individuals to
        # a list
        for _ in range(self.population_size):
            self.population.append(BitString(self.ind_size))

    def get_num_same(self) -> float:
        """Create a dictionary where each key is every unique individual in the
        population.

        The number of each individuals are counted.
        % unique = Total number with count > 2 / total individuals

        Returns
            % unique individuals in the population
        """
        # allows a default key in the dictionary with a default value of 0. 
        from collections import defaultdict
        num_stats = defaultdict(lambda: 0)
        # counts each unique individuals 
        for ind in self.population:
            num_stats[str(ind.fitness)] += 1
        # Sum the count of individuals whose count is higher than 1. Divide
        # that by the pop size to get % of unique individuals
        return 100*sum(filter(lambda i: i > 1, num_stats.values())) \
                / self.population_size

        return count / self.population_size


class FixedSize(Population):
    """Canonical Genetic Algorithm"""
    def __init__(self, pop_size) -> None:
        self.population_size = pop_size
        self.population = []

    def get_num_same(self) -> float:
        """Create a dictionary where each key is every unique individual in the
        population.

        The number of each individuals are counted.
        % unique = Total number with count > 2 / total individuals

        Returns
            % unique individuals in the population
        """
        # allows a default key in the dictionary with a default value of 0. 
        from collections import defaultdict
        num_stats = defaultdict(lambda: 0)
        # counts each unique individuals 
        for ind in self.population:
            num_stats[str(ind.val)] += 1
        # Sum the count of individuals whose count is higher than 1. Divide that
        # by the pop size to get % of unique individuals
        return len(num_stats.values())/ self.population_size * 100

    def calculate_fitness(self, fitness : Fitness):
        """Calculates the fitness of the entire population"""
        for indv in self.population:
            indv.fitness = fitness.return_fitness(indv)

