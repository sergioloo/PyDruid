from .package   import Package
from .project   import Project
from text       import Token
from utils      import Error


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
        if not self.current or self.current.type in types:
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

        

        self.__expect([Token.TOKT_EOF])
        self.__advance()

        return pkg

    def parse(self):
        proj = Project("kk") # TODO: Evidentemente, el proyecto no se llama kk

        while self.current:
            proj.add_package(self.__package())

        return proj
