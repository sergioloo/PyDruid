from .code_node import CodeNode
from utils      import Error


class Type(CodeNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # TODO: Aquí supongo que habrá que hacer algo... de momento queda en blanco,
        # pero vamos, que para eso escribo el método __init__
