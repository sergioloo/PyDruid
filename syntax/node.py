from utils import Error


class Node:
    def __init__(self, **kwargs):
        self.parent = kwargs['parent'] if 'parent' in kwargs else None
    
    def to_string(self) -> str:
        Error("uninitialized node.", type_=Error.INTERNAL_ERROR)
        return '' # No se puede alcanzar este código, es solo para que el linter no dé un error.
