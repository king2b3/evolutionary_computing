class Fitness(abc.ABC):
    def __init__(self) -> None:
        None

    @abstractmethod
    def returnFitness(self, individual) -> float:
        pass

class MaxOnes(Fitness):

    def returnFitness(self, individual) -> float:
        return sum(individual)/len(individual)

class Rosenbrock(Fitness):

    def returnFitness(self, individual) -> float:
        None