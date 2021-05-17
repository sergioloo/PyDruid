from .statement import Statement


class Block(Statement):
    def __init__(self, **kwargs):
        Statement.__init__(self, **kwargs)

        self.statements = []
    
    def add_statement(self, stt):
        self.statements.append(stt)
    
    def to_string(self):
        result = '{\n'

        for stt in self.statements:
            result += '\t' * stt.indent + f'{stt.to_string()};\n'

        result += '}\n'

        return result
