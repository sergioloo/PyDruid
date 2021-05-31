from syntax.abstract import *


class Function(Callable, Definition, Scope, Symbol):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.return_value = 'void'
    
    def get_prototype(self) -> str:
        return f'{self.return_value} {self.get_full_id()}();'
    
    def to_string(self):
        result = f'{self.return_value} {self.get_full_id()} () ' + '{\n'

        

        result += '}\n'        

        return result
    
    @staticmethod
    def new(dh: DefinitionHolder, name):
        return Definition.new(dh, Function, name, dh.funcs)
