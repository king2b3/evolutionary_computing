import abc
import random
random.seed()

class Individual(abc.ABC):
    
    def __init__(self) -> None:
        self.val = []

    @abc.abstractmethod
    def generate(self) -> None:
        pass

    @abc.abstractmethod
    def mutate(self) -> float:
        pass


class BitString(Individual):

    def __init__(self, size, num_of_variables) -> None:
        self.size = size
        self.num_of_variables = num_of_variables
        super().__init__()
        self.generate()

    def generate(self) -> None:
        self.val = random.choices([0,1],k=self.size)
    
    def mutate(self) -> None:
        location = random.randint(0,self.size-1) 
        self.val[location] = 1 - self.val[location]
    
def main():
    b = BitString(16,2)
    for _ in range(10):
        b.mutate()
        print(b.val)

if __name__ == "__main__":
    main()