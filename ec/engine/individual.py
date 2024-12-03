''' Abstract class for the individual structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''

import abc

class Individual(abc.ABC):
    """ Abstract structure for an individual.
          Initializes their fitness to 0.
    """
    def __init__(self) -> None:
        self.fit = 0
        self.fit_score = 0

    @abc.abstractmethod
    def generate(self) -> None:
        """Method to generate a random individual"""

    @abc.abstractmethod
    def mutate(self, mut_rate) -> float:
        """Method to mutate the individual"""

    @abc.abstractmethod
    def crossover(self, ind2) -> list:
        """Method to crossover the individual with another individual single
        point crossover.

        Might make mutate and crossover into their own child classes of
        individual later.
        """

    @abc.abstractmethod
    def __str__(self) -> str:
        """For visual representation when the instance is printed."""
