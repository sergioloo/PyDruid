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
        if not self.current or self.current.type not in types:
            expected = types[0]

            for i, t in enumerate(types):
                if i == 0:              continue
                if i == len(types) - 1: continue

                expected += f',{t}'
            
            if len(types) > 1: expected += f' or {types[len(types) - 1]}'

            if not self.current: Error(f"expecting {expected} and got nothing.")
            if not self.current.type in types: Error(f"expecting {expected} and got {self.current.type}.", tok=self.current)


    def __package(self):
        self.__expect([Token.TOKT_PACKAGE])
        self.__advance()

        # Vale, aquí la movida es que puede coger tokens de identificador y punto.
        # Todo esto lo tiene que convertir después a una cadena de texto, que se guardará
        # como string en un nodo de paquete.

        name_toks = []

        while self.current and self.current.type != Token.TOKT_SEMICOLON:
            self.__expect([Token.TOKT_ID])
            name_toks.append(self.current)
            self.__advance()

            self.__expect([Token.TOKT_DOT, Token.TOKT_SEMICOLON])
            if self.current.type == Token.TOKT_DOT: self.__advance()
        
        self.__advance()

        name = ''

        for i, t in enumerate(name_toks):
            if i == len(name_toks) - 1: name += t.value
            else:                       name += f'{t.value}_'

        # NOTE: Se supone que aquí es dónde tiene que buscar los atributos del
        # paquete.

        self.__expect([Token.TOKT_EOF])
        self.__advance()

        # Ahora crear el paquete
        pkg = Package(name, [], [], [])

        return pkg
    
    def parse(self):
        packages = []

        while self.current:
            packages.append(self.__package())

        ast = Project("test", packages)
        # TODO: Cambia 'test' por el nombre original del proyecto

        return ast
