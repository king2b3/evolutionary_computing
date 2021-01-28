import abc
import random
random.seed()
from individual import BitString

class Population(abc.ABC):
    
    def __init__(self, pop_size) -> None:
        self.pop_size = pop_size
        self.pop = []

    @abc.abstractmethod
    def generate(self, ind_size, num_of_variables) -> None:
        pass


class CGA(Population):

    def __init__(self, pop_size, ind_size, num_of_variables) -> None:
        super().__init__(pop_size)
        self.generate(ind_size,num_of_variables)

    def generate(self, ind_size, num_of_variables) -> None:
        for _ in range(self.pop_size):
            self.pop.append(BitString(ind_size,num_of_variables))
    

def main():
    b = CGA(10,4,2)
    print(b.pop)

if __name__ == "__main__":
    main()