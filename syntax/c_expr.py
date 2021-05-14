from .statement import Statement


class CExpr(Statement):
    def __init__(self, expr, container):
        super().__init__(self.ST_CEXPR, container)
        self.value = expr
    
    def to_c(self):
        return self.value
