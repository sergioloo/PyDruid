from syntax.abstract import *


class Function(Callable, Definition, Scope, Symbol):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @staticmethod
    def new(dh: DefinitionHolder, name):
        return Definition.new(dh, Function, name, dh.funcs)
