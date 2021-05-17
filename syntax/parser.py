from .ast               import AST
from .bin_op            import BinOp
from .class_            import Class
from .container         import Container
from .factor            import Factor
from .method            import Method
from .package           import Package
from .return_statement  import ReturnStatement
from .symbol            import Symbol
from text               import Token
from utils              import Error


class Parser:
    def __init__(self, toks):
        self.toks       = toks
        self.index      = -1
        self.current    = None

        self.__advance()

    def __advance(self):
        self.index += 1
        self.current = self.toks[self.index] if self.index < len(self.toks) else None

    def __expect(self, types):
        if not self.current or self.current.type not in types:
                expected = types[0]

                for i, t in enumerate(types):
                    if    i == 0:               continue
                    elif  i == len(types) - 1:  expected += f' or {t}'
                    else:                       expected += f', {t}'
                
                if not self.current:                Error(f"expecting {expected} and got nothing.")
                if self.current.type not in types:  Error(f"expecting {expected} and got {self.current.type}", tok=self.current)
    
    def __is_token_type(self, types):
        return self.current and self.current.type in types
    
    def __is_not_token_type(self, types):
        return self.current and self.current.type not in types
    
    def __get_id(self) -> str:
        toks = []

        while self.__is_token_type([Token.TOKT_ID]):
            toks.append(self.current)
            self.__advance()

            if self.__is_token_type([Token.TOKT_DOT]):
                toks.append(self.current)
                self.__advance()
        
        result = ''

        for tok in toks: result += tok.value if tok.type == Token.TOKT_ID else '_'

        return result
    
    def __fill_container(self, container: Container, init_mark=Token.TOKT_LCBRACK, final_mark=Token.TOKT_RCBRACK):
        if init_mark:
            self.__expect([init_mark])
            self.__advance()

        while self.__is_not_token_type([final_mark]):
            # Obtener parámetros
            id_ = self.__get_id()

            self.__expect([Token.TOKT_DEF])
            self.__advance()

            vb = Symbol.VB_PROTECTED
            if self.__is_token_type([Token.TOKT_PUBLIC, Token.TOKT_PROTECTED, Token.TOKT_PRIVATE]):
                if   self.current.type == Token.TOKT_PUBLIC:    vb = Symbol.VB_PUBLIC
                elif self.current.type == Token.TOKT_PROTECTED: vb = Symbol.VB_PROTECTED
                elif self.current.type == Token.TOKT_PRIVATE:   vb = Symbol.VB_PRIVATE

                self.__advance()
            
            static = False
            if self.__is_token_type([Token.TOKT_STATIC]):
                static = True
                self.__advance()

            final = False
            if self.__is_token_type([Token.TOKT_FINAL]):
                final = True
                self.__advance()

            self.__expect([Token.TOKT_CLASS, Token.TOKT_ID])
            
            type_ = None
            if self.current.type == Token.TOKT_ID: type_ = self.__get_id()
            else: 
                type_ = self.current
                self.__advance()

            # Añadir elemento al contenedor
            if isinstance(type_, Token) and type_.type == Token.TOKT_CLASS: container.add_class(self.__class(id_, vb, static, container))
            else: container.add_method(self.__method(id_, type_, container, vb, static, final))

        self.__advance()
    
    def __fill_block(self, block):
        self.__expect([Token.TOKT_LCBRACK])
        self.__advance()

        while self.__is_not_token_type([Token.TOKT_RCBRACK]):
            if self.current.type == Token.TOKT_RETURN: block.add_statement(self.__return(block))

            self.__expect([Token.TOKT_SEMICOLON, Token.TOKT_RCBRACK])
            if self.current.type == Token.TOKT_SEMICOLON: self.__advance()

        self.__expect([Token.TOKT_RCBRACK])
        self.__advance()
    
    def __factor(self, parent):
        self.__expect([Token.TOKT_INT, Token.TOKT_FLOAT, Token.TOKT_ID])

        fact = Factor(value=self.current.value, parent=parent)
        self.__advance()

        return fact
    
    def __term(self, parent):
        left = self.__factor(parent)
        
        while self.__is_token_type([Token.TOKT_MULT, Token.TOKT_DIV, Token.TOKT_POW]):
            op = None
            if   self.current.type == Token.TOKT_MULT:  op = BinOp.OP_MULT
            elif self.current.type == Token.TOKT_DIV:   op = BinOp.OP_DIV
            elif self.current.type == Token.TOKT_POW:   op = BinOp.OP_POW
            self.__advance()

            right = self.__term(parent)

            old_left = left
            left = BinOp(left=left, op=op, right=right, parent=parent)
        
        return left
    
    def __expression(self, parent):
        left = self.__term(parent)
        
        while self.__is_token_type([Token.TOKT_PLUS, Token.TOKT_MINUS]):
            op = None
            if   self.current.type == Token.TOKT_PLUS:  op = BinOp.OP_ADD
            elif self.current.type == Token.TOKT_MINUS: op = BinOp.OP_SUBT
            self.__advance()

            right = self.__expression(parent)

            old_left = left
            left = BinOp(left=left, op=op, right=right, parent=parent)
        
        return left
    
    def __return(self, block):
        rs = ReturnStatement(parent=block)

        self.__expect([Token.TOKT_RETURN])
        self.__advance()

        val = self.__expression(rs)
        rs.set_return_value(val)

        return rs
    
    def __method(self, id_, type_, parent,
        visibility   = Symbol.VB_PROTECTED,
        static: bool = False,
        final:  bool = False
    ):
        mthd = Method(
            id          = id_,
            type        = type_,
            visibility  = visibility,
            static      = static,
            final       = final,
            parent      = parent
        )

        self.__expect([Token.TOKT_LPAREN])
        self.__advance()

        self.__expect([Token.TOKT_RPAREN])
        self.__advance()

        self.__expect([Token.TOKT_LCBRACK])
        self.__fill_block(mthd)

        return mthd
    
    def __class(
        self,
        id_: str,
        vb: str,
        static: bool,
        parent_scope
    ):
        cls_ = Class(
            id          = id_,
            visibility  = vb,
            static      = static,
            parent      = parent_scope
        )

        self.__fill_container(cls_)

        return cls_
    
    def __package(self, root_scope):
        self.__expect([Token.TOKT_PACKAGE])
        self.__advance()

        id_: str = self.__get_id()

        self.__expect([Token.TOKT_SEMICOLON])
        self.__advance()

        pkg = Package(
            id      = id_,
            parent  = root_scope
        )

        self.__fill_container(pkg, init_mark=None, final_mark=Token.TOKT_EOF)

        return pkg
        
    def parse(self):
        ast = AST()

        while self.current:
            ast.add_package(self.__package(ast))

        return ast
