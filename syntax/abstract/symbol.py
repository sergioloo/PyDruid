from .code_node import CodeNode
from syntax     import Accessibility


class Symbol(CodeNode):
    def __init__(self, name, visibility=Accessibility.public(), **kwargs):
        super().__init__(**kwargs)

        self.name       = name
        self.visibility = visibility
    
    def get_full_id(self) -> str:
        parent = self.parent
        result = self.name

        while parent and isinstance(parent, Symbol):
            result = f'{parent.name}_{result}'
            parent = parent.parent
        
        return result
    
    def get_virtual_id(self) -> str:
        parent = self.parent
        result = self.name

        while parent and isinstance(parent, Symbol):
            result = f'{parent.name}.{result}'
            parent = parent.parent
        
        return result
