from .container import Container
from .symbol    import Symbol


class Package(Container):
    def __init__(self, **kwargs):
        Container.__init__(self, **kwargs)

        del self.visibility
        del self.static
        del self.final
    
    def to_string(self, mode=None) -> str:
        result = f'// Package {self.id}\n\n'

        for cls_ in self.classes:
            result += cls_.to_string(Symbol.TM_DEFINITION)

        return result
