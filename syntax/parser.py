from .class_        import Class
from .initializer   import Initializer
from .package       import Package
from .project       import Project
from text           import Token
from utils          import Error


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
    
    def __get_id(self):
        self.__expect([Token.TOKT_ID])
        
        toks = []
        while self.current and self.current.type == Token.TOKT_ID:
            toks.append(self.current)
            self.__advance()

            if self.current and self.current.type == Token.TOKT_DOT:
                toks.append(self.current)
                self.__advance()
        
        result = ''

        for tok in toks:
            if tok.type == Token.TOKT_DOT:  result += '_'
            else:                           result += tok.value
        
        return result
    
    def __package(self):
        self.__expect([Token.TOKT_PACKAGE])
        self.__advance()

        id_ = self.__get_id()

        self.__expect([Token.TOKT_SEMICOLON])
        self.__advance()

        pkg = Package(id_)

        while self.current and self.current.type != Token.TOKT_EOF:
            init = self.__initializer()

            if init.type == Initializer.ST_CLASS: pkg.add_class(self.__class(init))

        self.__expect([Token.TOKT_EOF])
        self.__advance()

        return pkg
    
    def __class(self, init):
        class_ = Class(init)

        self.__expect([Token.TOKT_LCBRACK])
        self.__advance()

        self.__expect([Token.TOKT_RCBRACK])
        self.__advance()

        return class_

    def __initializer(self):
        id_ = self.__get_id()

        self.__expect([Token.TOKT_DEF])
        self.__advance()

        vb = Initializer.VB_PROTECTED

        if self.current and self.current.type in (Token.TOKT_PUBLIC, Token.TOKT_PROTECTED, Token.TOKT_PRIVATE):
            if      self.current.type == Token.TOKT_PUBLIC:     vb = Initializer.VB_PUBLIC
            elif    self.current.type == Token.TOKT_PROTECTED:  vb = Initializer.VB_PROTECTED
            elif    self.current.type == Token.TOKT_PRIVATE:    vb = Initializer.VB_PRIVATE

            self.__advance()
        
        static = False
        
        if self.current and self.current.type == Token.TOKT_STATIC:
            static = True
            self.__advance()
        
        final = False
        if self.current and self.current.type == Token.TOKT_FINAL:
            final = True

        type_ = None

        self.__expect([Token.TOKT_CLASS, Token.TOKT_ID])

        if self.current.type == Token.TOKT_ID:
            type_ = self.__get_id()

        elif self.current.type == Token.TOKT_CLASS:  
            type_ = Initializer.ST_CLASS
            self.__advance()
        
        return Initializer(id_, vb, static, final, type_)

    def parse(self):
        proj = Project("kk") # TODO: Evidentemente, el proyecto no se llama kk

        while self.current:
            proj.add_package(self.__package())

        return proj
