from utils import Error


class Node:
    # Debería llamarse ASTNode, pero es más difícil de escribir
    NT_AST          = 'abstract syntax tree'
    NT_PKG          = 'package'
    NT_CLASS        = 'class'
    NT_ID           = 'identifier'

    NR_ID           = 'identifier'
    NR_SCOPE        = 'scope'
    NR_VALUE        = 'value'


    def __init__(self, type_, ctx):
        self.type       = type_
        self.ctx        = ctx

        self.registers  = {}
    
    def register(self, key, value):
        self.registers[key] = value
    
    def retrieve(self, key):
        obj = self.registers.get(key)
        if not obj: Error(
            f"development error. attemped to access a {key} register from a {self.type} node.",
            type_="internal error"
        )
        return obj
