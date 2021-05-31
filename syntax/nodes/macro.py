from syntax.abstract import *


class Macro(Callable, Definition, Scope, Symbol):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        pass

    @staticmethod
    def new(dh: DefinitionHolder, name):
        return Definition.new(dh, Macro, name, dh.macros)
    
    def to_string(self):
        args = self.args[0] if len(self.args) > 0 else ''

        for i, a in enumerate(self.args):
            if   i == 0:                    continue
            elif i == len(self.args):       args += a
            else:                           args += f', {a}'

        result = f'#define {self.get_full_id()}({args})'
        return result
