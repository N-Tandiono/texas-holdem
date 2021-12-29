from strategy.strategy import Strategy
from table import Table


class PushStrategy(Strategy):
    def generate_move(self, table: Table) -> str:
        return "r 200"