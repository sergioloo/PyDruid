from syntax.block   import Block
from .container     import Container


class Method(Container):
    def __init__(self, init, type_, args, parent):
        super().__init__(init.id, parent)

        self.init   = init
        self.type   = type_ # Tipo de valor de retorno
        self.args   = args
        self.block  = Block()
    
    def __repr__(self):
        return f"[Method {self.init.id}]"
    
    def set_block(self, blk):
        self.block = blk

    def get_prototype(self):
        return f'{self.type} {self.get_full_id()}()'
    
    def get_pointer(self):
        return f'{self.type} (*{self.id})()'
    
    def to_c(self):
        return self.get_prototype() + self.block.to_c()
