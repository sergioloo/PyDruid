from .accessibility import Accessibility
from .code_node import CodeNode


class Symbol(CodeNode):
    """
    Per se, any node of the AST can be a Symbol. When you open VSCode, there's a lap
    at the bottom left which is called "outline". That lap contains all the symbols
    defined inside a file.
    So every definition is a symbol. A definition of a class, of a macro, of a method...
    Pretty much every definition.
    """

    def __init__(
        self, 
        name, 
        accessibility=Accessibility.public(), 
        **kwargs
    ):
        super().__init__(**kwargs)

        self.name: str                      = name          # This is the name of the symbol as string
        self.accessibility: Accessibility   = accessibility # Accessibility to the symbol from outer scopes
