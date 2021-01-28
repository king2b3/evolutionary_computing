class Selection(abc.ABC):
    def __init__(
        self
    ) -> None:

    @abstractmethod
    def returnSelection(
        self
    ) -> None:
        pass

class RouletteWheelSelection(Selection):

    def returnSelection(
        self
    ) -> float:
        None