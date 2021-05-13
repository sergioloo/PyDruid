from .statement import Statement


class Factor(Statement):
    def __init__(self, value):
        super().__init__(self.ST_FACTOR)
        self.value = value

    def to_c(self):
        return self.value
