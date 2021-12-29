from strategy.strategy import Strategy
from table import Table


class FoldStrategy(Strategy):
    def generate_move(self, table: Table) -> str:
        return "fold"