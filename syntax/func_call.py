from .statement import Statement


class FunctionCall(Statement):
    def __init__(self, func, args):
        super().__init__(self.ST_FUNC_CALL)
        
        self.function   = func
        self.args       = args

    def to_c(self):
        args = ''

        for i, a in enumerate(self.args):
            if i == 0: args += a.to_c()
            else:      f', {a}'

        return f'{self.function.to_c()}({args})'
