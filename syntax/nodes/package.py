from syntax.abstract import DefinitionHolder
from syntax.abstract import Symbol


class Package(Symbol, DefinitionHolder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get_prototype(self) -> str:
        result = ''

        for obj_ in self.definitions:
            result += obj_.get_prototype() + '\n'
        
        return result
        
    def to_string(self):
        result = f'// Package {self.get_virtual_id()} \n'

        for cls_ in self.classes:
            result += cls_.to_string()

        return result
