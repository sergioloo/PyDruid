from .code_node import CodeNode
from syntax     import Accessibility


class Symbol(CodeNode):
    def __init__(self, name, visibility=Accessibility.public(), **kwargs):
        super().__init__(**kwargs)

        self.name       = name
        self.visibility = visibility
