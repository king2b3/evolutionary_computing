""" Holds the base selection structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""
import abc

class Selection(abc.ABC):
    """Base class for the selection functions"""
    def __init__(self, selection_size : int):
        """Initialization of the abstract selection function
        """
        self.sel_size = selection_size

    @abc.abstractmethod
    def __call__(self, pop) -> list:
        """Returns the parent population"""

