from abc import ABC, abstractmethod


class Tires(ABC):

    def __init__(self, tires_worned: list):
        self.tires_worned = tires_worned

    @abstractmethod
    def needs_service(self) -> bool:
        pass
