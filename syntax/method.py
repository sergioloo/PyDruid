from .container import Container


class Method(Container):
    def __init__(self, init, type_, args, parent):
        super().__init__(init.id, parent)

        self.init   = init
        self.type   = type_ # Tipo de valor de retorno
        self.args   = args
    
    def __repr__(self):
        return f"[Method {self.init.id}]"
