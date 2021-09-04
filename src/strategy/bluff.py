from strategy.strategy import Strategy
from table import Table


class BluffStrategy(Strategy):
    def generate_move(self, table: Table) -> str:
        return "check"