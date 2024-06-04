class Ratio:
    def __init__(self,ratio_id, strategy_id, ratio, ratio2, type, category, operator, value, must_match):
        self.ratio_id = ratio_id
        self.strategy_id = strategy_id
        self.ratio = ratio
        self.ratio2 = ratio2
        self.type = type
        self.category = category
        self.operator = operator
        self.value = value
        self.must_match = must_match