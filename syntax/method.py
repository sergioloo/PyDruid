from .symbol    import Symbol
from utils      import Error


class Method(Symbol):
    def __init__(self, **kwargs):
        Symbol.__init__(self, **kwargs)

        self.type = kwargs['type'] if 'type' in kwargs else Error("return type for method not specified.")

        self.statements = []
    
    def add_statement(self, stt):
        self.statements.append(stt)
    
    def to_string(self, mode):
        full_id = self.get_full_id()

        if mode == Symbol.TM_PROTOTYPE:
            return f'{"static " if self.static else ""}{self.type} {full_id}(); \n'
        
        elif mode == Symbol.TM_DEFINITION:
            result = f'{"static " if self.static else ""}{self.type} {full_id}() ' + '{\n'

            for stt in self.statements:
                result += '\t' * stt.indent + f'{stt.to_string()};\n'

            result += '}\n'

            return result
