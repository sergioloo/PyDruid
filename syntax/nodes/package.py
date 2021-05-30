from syntax.abstract import DefinitionHolder
from syntax.abstract import Symbol


class Package(Symbol, DefinitionHolder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
