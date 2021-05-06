from .ast_node      import Node
from .context_node  import ContextNode
from text           import Token
from utils          import Error


class Parser:
    def __init__(self, file_, toks):
        self.file       = file_

        self.toks       = toks
        self.index      = -1
        self.current    = None

        self.__advance()

    def __advance(self):
        self.index      += 1
        self.current    =  self.toks[self.index] if self.index < len(self.toks) else None
    
    def __expect(self, types):
        if not self.current or self.current.type not in types:
            expected = types[0]

            for i, t in enumerate(types):
                if i == 0:              continue
                if i == len(types) - 2: break

                expected += f', {t}'
            
            expected += f'or {types[len(types) - 1]}'

            if not self.current: Error(f"expecting {expected} and got nothing.")
            Error(f"expecting {expected} and got {self.current.type}.", tok=self.current)

    
    # Métodos de nodos
    def __id(self, ctx):
        self.__expect([Token.TOKT_ID])

        value = []

        while self.current and self.current.type not in (Token.TOKT_ID, Token.TOKT_DOT):
            self.__expect([Token.TOKT_ID])
            value += self.current
            self.__advance()

            if self.current and self.current.type == Token.TOKT_DOT:
                self.__advance()
        
        node = Node(Node.NT_ID, ctx)
        node.register(Node.NR_VALUE, value)

        return node
    
    def __class(self, ctx):
        pass
    
    def __package(self, ctx):
        self.__expect([Token.TOKT_PACKAGE])
        self.__advance()

        id_ = self.__id(ctx)

        self.__expect([Token.TOKT_SEMICOLON])
        self.__advance()

        # Obtener el nombre en C del paquete
        pkg_name = ''
        
        for i, t in enumerate(id_.retrieve(Node.NR_VALUE)):
            if i == 0: 
                pkg_name += t.value
                continue

            pkg_name += f'_{t}'
        
        # Crear un contexto interno
        inner_ctx = ContextNode(pkg_name, ContextNode.CNT_PKG, parent=ctx)


        
        self.__expect([Token.TOKT_EOF])
        
        # Crear el nodo de paquete
        node = Node(Node.NT_PKG, ctx)
        node.register(Node.NR_ID, id_)

        return node

    # Método de análisis
    def parse(self):
        root_ctx = ContextNode(self.file, ContextNode.CNT_ROOT)

        source = []
        while self.current:
            source.append(self.__package(root_ctx))
        
        node = Node(Node.NT_AST, root_ctx)
        node.register(Node.NR_SCOPE, source)

        return node
