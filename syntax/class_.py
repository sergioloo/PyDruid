from .container import Container


class Class(Container):
    def __init__(self, init, parent):
        super().__init__(init.id, parent)
        self.init = init
    
    def __repr__(self):
        return f"[Class {self.init.id}]"
