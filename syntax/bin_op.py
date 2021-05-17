from .statement import Statement


class BinOp(Statement):
    OP_ADD          = 'addition'
    OP_SUBT         = 'subtraction'
    OP_MULT         = 'multiplication'
    OP_DIV          = 'division'
    OP_POW          = 'power'

    def __init__(self, **kwargs):
        Statement.__init__(self, **kwargs)

        self.left    = kwargs['left'] if 'left' in kwargs else None
        self.op      = kwargs['op'] if 'op' in kwargs else None
        self.right   = kwargs['right'] if 'right' in kwargs else None
    
    def set_left(self, n):  self.left   = n
    def set_op(self, op):   self.op     = op
    def set_right(self, n): self.right  = n

    def to_string(self):
        if   self.op == self.OP_ADD:    return f'{self.left.to_string()} + {self.right.to_string()}'
        elif self.op == self.OP_SUBT:   return f'{self.left.to_string()} - {self.right.to_string()}'
        elif self.op == self.OP_MULT:   return f'{self.left.to_string()} * {self.right.to_string()}'
        elif self.op == self.OP_DIV:    return f'{self.left.to_string()} / {self.right.to_string()}'
        elif self.op == self.OP_POW:    return f'pow({self.left.to_string()}, {self.right.to_string()})'
