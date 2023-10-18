""" Abstract class for the individual structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""

import abc

class Individual(abc.ABC):
    """Abstract structure for an individuals in a population."""
    def __init__(self):
        self.fit = 0
        self.fit_score = 0

    @abc.abstractmethod
    def generate(self):
        """Generates a new random individual"""

    @abc.abstractmethod
    def mutate(self, mut_rate):
        """Mutatea the individual

        Parameters:
            mut_rate (float): mutation rate
        """

    @abc.abstractmethod
    def crossover(self, ind2):
        """Method to crossover the individual with another individual single point crossover.

        Parameters:
            individual_2 (Individual): the 2nd individual used for crossover

        Returns:
            list(Individuals): both the children from the crossover operation
        """

    @abc.abstractmethod
    def __str__(self):
        """For visual representation when the instance is printed

        Returns:
            Some representation for visualization"""
