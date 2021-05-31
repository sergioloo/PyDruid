from .abstract      import *
from .nodes         import *
from text           import Token
from utils          import Error


class Parser:
    def __init__(self, name, toks):
        self.name       = name
        self.toks       = toks
        self.tok_idx    = -1
        self.current    = None

        self.next()
    
    def next(self):
        self.tok_idx    += 1
        self.current    =  self.toks[self.tok_idx] if self.tok_idx < len(self.toks) else None
        return self.current

    def expect(self, types):
        if not self.current or self.current.type not in types:
                expected = types[0]

                for i, t in enumerate(types):
                    if    i == 0:               continue
                    elif  i == len(types) - 1:  expected += f' or {t}'
                    else:                       expected += f', {t}'
                
                if not self.current:                Error(f"expecting {expected} and got nothing.")
                if self.current.type not in types:  Error(f"expecting {expected} and got {self.current.type}", tok=self.current)
        
    def expect_and_continue(self, types):
        self.expect(types)
        self.next()
    
    def is_token_type(self, types):
        return self.current and self.current.type in types
    
    def is_not_token_type(self, types):
        return self.current and self.current.type not in types
    
    def get_id(self) -> str:
        toks = []

        while self.is_token_type([Token.TOKT_ID]):
            toks.append(self.current)
            self.next()

            if self.is_token_type([Token.TOKT_DOT]):
                toks.append(self.current)
                self.next()
        
        result = ''

        for tok in toks: result += tok.value if tok.type == Token.TOKT_ID else '_'

        return result
    
    def semicolon(self):
        # NOTE. Para ser implementado. No es de mis mayores preocupaciones.

        if self.is_token_type([Token.TOKT_SEMICOLON]): self.next()
    
    def fill_definition_holder(self, dh: DefinitionHolder, end_tok=Token.TOKT_RCBRACK):
        while self.is_not_token_type([end_tok]):
            self.expect([
                Token.TOKT_CLASS, Token.TOKT_STRUCT, Token.TOKT_ENUM, Token.TOKT_FUNCTION, Token.TOKT_MACRO
            ])
            type_ = self.current.type
            self.next()

            name = self.get_id()

            if      type_ == Token.TOKT_CLASS:      self.class_(dh, name)
            elif    type_ == Token.TOKT_FUNCTION:   self.function(dh, name)
            else:   self.next()
        
        self.next()
    
    def function(self, dh: DefinitionHolder, name):
        func = Function.new(dh, name)

        # get arguments
        self.expect_and_continue([Token.TOKT_LPAREN])
        while self.is_not_token_type([Token.TOKT_RPAREN]):
            self.next()
        
        self.next()

        self.expect_and_continue([Token.TOKT_LCBRACK])
        while self.is_not_token_type([Token.TOKT_RCBRACK]):
            self.next()
        
        self.next()
        
    def class_(self, dh: DefinitionHolder, name):
        cls_ = Class.new(dh, name)

        self.expect_and_continue([Token.TOKT_LCBRACK])
        self.fill_definition_holder(cls_)

    def package(self, ast: AST):
        self.expect_and_continue([Token.TOKT_PACKAGE])
        name = self.get_id()
        
        pkg: Package = ast.get_package(name)
        self.fill_definition_holder(pkg, end_tok=Token.TOKT_EOF)
            
    def parse(self):
        ast = AST(self.name)

        while self.current:
            self.package(ast)
        
        return ast
