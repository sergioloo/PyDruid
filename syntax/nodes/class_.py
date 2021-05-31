from syntax.nodes.constructor import Constructor
from syntax.abstract import *


class Class(Symbol, DefinitionHolder, Definition, Type):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.constructor = Constructor(self)

    @staticmethod
    def new(dh, name):
        return Definition.new(dh, Class, name, dh.classes)
    
    def get_prototype(self) -> str:
        result = ''

        result += f'struct _{self.get_full_id()}; \n'
        result += f'typedef struct _{self.get_full_id()} _{self.get_full_id()}; \n'
        result += f'typedef struct _{self.get_full_id()} *{self.get_full_id()}; \n'
        result += self.constructor.get_prototype() + '\n'

        for obj_ in self.definitions:
            result += obj_.get_prototype() + '\n'
        
        return result

    def to_string(self):
        result = f'// Class {self.get_virtual_id()} \n'

        result += f'typedef struct _{self.get_full_id()} ' + '{\n'

        for method in self.funcs:
            result += f'\t{method.return_value} (*{method.name}) ();\n'

        result += '}' + f' _{self.get_full_id()}; \n\n'

        result += self.constructor.to_string() + '\n'

        for method in self.funcs:
            result += method.to_string()

        return result
