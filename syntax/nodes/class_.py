from syntax.abstract import *


class Class(Symbol, DefinitionHolder, Definition, Type):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def new(dh, name):
        return Definition.new(dh, Class, name, dh.classes)
