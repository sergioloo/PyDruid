from .statement import Statement
from utils      import Error


class BinOp(Statement):
    OP_ADDITION = 'addition'
    OP_SUBT     = 'subtraction'
    OP_MULT     = 'multiplication'
    OP_DIV      = 'division'
    OP_POW      = 'power'

    def __init__(self, left, op, right):
        super().__init__(type_=self.ST_BIN_OP)
        self.left   = left
        self.op     = op
        self.right  = right

    def to_c(self):
        if   self.op == self.OP_ADDITION:   return f'{self.left.to_c()} + {self.right.to_c}'
        elif self.op == self.OP_SUBT:       return f'{self.left.to_c()} - {self.right.to_c}'
        elif self.op == self.OP_MULT:       return f'{self.left.to_c()} * {self.right.to_c}'
        elif self.op == self.OP_DIV:        return f'{self.left.to_c()} / {self.right.to_c}'
        elif self.op == self.OP_POW:        return f'pow({self.left.to_c()}, {self.right.to_c})'
        else:                               Error("invalid operation node.")
