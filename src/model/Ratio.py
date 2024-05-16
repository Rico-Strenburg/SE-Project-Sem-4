class Ratio:
    def __init__(self,ratio_id, strategy_id, ratio, operator, value, must_match):
        self.ratio_id = ratio_id
        self.strategy_id = strategy_id
        self.ratio = ratio
        self.operator = operator
        self.value = value
        self.must_match = must_match