from text.token import Token
from .statement import Statement


class Atom(Statement):
    def __init__(self, value, container):
        super().__init__(self.ST_ATOM, container)
        
        self.value: Token = value
    
    def to_c(self):
        if      self.value.type == Token.TOKT_ID:       return self.parent.get_inner_id(self.value.value)
        elif    self.value.type == Token.TOKT_STRING:   return f'"{self.value.value}"'
        return self.value.value
