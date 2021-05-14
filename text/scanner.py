from .position  import Position
from .token     import Token
from string     import ascii_letters
from utils      import Error


class Scanner:
    NUMBERS         = '0123456789'
    START_DIGITS    = '_' + ascii_letters
    DIGITS          = START_DIGITS + NUMBERS

    def __init__(self, file_):
        self.pos        = Position(0, 0, 0, file_.read(), file_.name)
        self.current    = self.pos.char
    
    def __advance(self):
        self.current = self.pos.advance()

    # Métodos de comentarios
    def __on_single_line_comment(self):
        while self.current and self.current != '\n':
            self.__advance()
    
    def __on_multiple_line_comment(self):
        while self.current:
            if self.current == '*':
                self.__advance()

                if self.current == '/':
                    self.__advance()
                    break

            self.__advance()

    # Métodos de palabras
    def __on_keyword(self):
        value   = ''
        start   = self.pos.copy()

        while self.current and self.current in self.DIGITS:
            value += self.current
            self.__advance()
        
        end     = self.pos.copy()

        if      value == 'public':      return Token(Token.TOKT_PUBLIC,     start, end)
        elif    value == 'protected':   return Token(Token.TOKT_PROTECTED,  start, end)
        elif    value == 'private':     return Token(Token.TOKT_PRIVATE,    start, end)
        elif    value == 'package':     return Token(Token.TOKT_PACKAGE,    start, end)
        elif    value == 'class':       return Token(Token.TOKT_CLASS,      start, end)
        elif    value == 'static':      return Token(Token.TOKT_STATIC,     start, end)
        elif    value == 'final':       return Token(Token.TOKT_FINAL,      start, end)
        elif    value == 'import':      return Token(Token.TOKT_IMPORT,     start, end)
        elif    value == 'return':      return Token(Token.TOKT_RETURN,     start, end)
        return                                 Token(Token.TOKT_ID,         start, end, value)
    
    def __on_string(self):
        value   = ''
        start   = self.pos.copy()

        self.__advance()

        while self.current and self.current != '"':
            value += self.current
            self.__advance()
        
        self.__advance()

        end = self.pos.copy()

        return Token(Token.TOKT_STRING, start, end, value)

    def __on_number(self):
        value       = ''
        start       = self.pos.copy()
        is_float    = False
        err_pos     = None

        while self.current and self.current in self.NUMBERS + '.':
            if self.current == '.':
                if is_float:    err_pos     = self.pos.copy()
                else:           is_float    = True

            value += self.current
            self.__advance()
        
        if err_pos: Error(F"illegal number: '{value}'.", pos=err_pos)

        end = self.pos.copy()

        return Token(
            Token.TOKT_FLOAT if is_float else Token.TOKT_INT,
            start, end,
            value
        )
    
    def __on_cexpr(self):
        value = ''
        start = self.pos.copy()

        self.__advance()
        
        if self.current != '[': Error("expecting '[' after '!'.", self.pos.copy())
        self.__advance()

        while self.current and self.current != ']':
            value += self.current
            self.__advance()
        
        self.__advance()

        end = self.pos.copy()

        return Token(Token.TOKT_CEXPR, start, end, value)

    # Método de escaneo    
    def scan(self):
        result = []

        while self.current:
            if self.current in ' \t\n': self.__advance()

            elif self.current == '.':
                result.append(Token(Token.TOKT_DOT, self.pos.copy()))
                self.__advance()
            
            elif self.current == ',':
                result.append(Token(Token.TOKT_COMMA, self.pos.copy()))
                self.__advance()

            elif self.current == ';':
                result.append(Token(Token.TOKT_SEMICOLON, self.pos.copy()))
                self.__advance()
            
            elif self.current == '{':
                result.append(Token(Token.TOKT_LCBRACK, self.pos.copy()))
                self.__advance()
            
            elif self.current == '}':
                result.append(Token(Token.TOKT_RCBRACK, self.pos.copy()))
                self.__advance()
            
            elif self.current == '(':
                result.append(Token(Token.TOKT_LPAREN, self.pos.copy()))
                self.__advance()
            
            elif self.current == ')':
                result.append(Token(Token.TOKT_RPAREN, self.pos.copy()))
                self.__advance()
            
            elif self.current == '+':
                result.append(Token(Token.TOKT_PLUS, self.pos.copy()))
                self.__advance()
            
            elif self.current == '-':
                result.append(Token(Token.TOKT_MINUS, self.pos.copy()))
                self.__advance()
            
            elif self.current == '*':
                result.append(Token(Token.TOKT_MULT, self.pos.copy()))
                self.__advance()

            elif self.current == '^':
                result.append(Token(Token.TOKT_POW, self.pos.copy()))
                self.__advance()
            
            elif self.current == ':':
                start = self.pos.copy()
                self.__advance()

                if self.current == ':':
                    result.append(Token(Token.TOKT_DEF, start, self.pos.copy()))
                    self.__advance()
                
                else:
                    Error("expecting '::'", pos=start)

            elif self.current in self.NUMBERS:      result.append(self.__on_number())
            elif self.current in self.START_DIGITS: result.append(self.__on_keyword())
            elif self.current == '"':               result.append(self.__on_string())
            elif self.current == '!':               result.append(self.__on_cexpr())
            
            elif self.current == '/':
                pos = self.pos.copy()
                self.__advance()

                if self.current == '/':
                    self.__advance()
                    self.__on_single_line_comment()
                
                elif self.current == '*':
                    self.__on_multiple_line_comment()
                
                else: result.append(Token(Token.TOKT_DIV, pos))
            
            else:
                Error(f"illegal character: '{self.current}'.", pos=self.pos.copy())
            
        result.append(Token(Token.TOKT_EOF, self.pos.copy()))

        return result
