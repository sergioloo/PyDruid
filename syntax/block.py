from .statement import Statement


class Block(Statement):
    def __init__(self, **kwargs):
        Statement.__init__(self, **kwargs)

        self.statements = []
    
    def add_statement(self, stt):
        self.statements.append(stt)
