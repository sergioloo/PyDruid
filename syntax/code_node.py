class CodeNode:
    """
    The documentation of this things needs to be written. Elseways it would be
    quite a nightmare to understand how the AST works... because even I'm having
    trouble by writing it.

    This is the CodeNode. It's the parent object for all derived nodes that will
    be branches of the abstract syntax tree, so every single node must inherit from
    this object.
    """

    def __init__(self, parent):
        self.parent = parent
    
    def to_string(self): return ""
