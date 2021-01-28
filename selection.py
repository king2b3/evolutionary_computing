class Selection(abc.ABC):
    def __init__(self) -> None:

    @abstractmethod
    def returnSelection(self, pop) -> list:
        pass

class RouletteWheelSelection(Selection):

    def returnSelection(self, pop) -> list:
        None