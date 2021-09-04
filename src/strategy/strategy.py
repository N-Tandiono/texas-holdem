from abc import ABC, abstractmethod

from table import Table

class Strategy(ABC):
    @abstractmethod
    def generate_move(self, table: Table) -> str:
        pass