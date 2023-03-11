''' Holds the base selection structure.

    Created on: 1-27-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
'''
import abc

class Selection(abc.ABC):
    def __init__(self) -> None:
        ''' Abstract class for the selection function
        '''
        pass

    @abc.abstractmethod
    def returnSelection(self, pop) -> list:
        ''' Returns the parent population
        '''
        pass
