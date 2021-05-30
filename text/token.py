class Token:
    TOKT_PACKAGE    = 'package'
    TOKT_CLASS      = 'class'
    TOKT_STRUCT     = 'struct'
    TOKT_ENUM       = 'enum'
    TOKT_FUNCTION   = 'function'
    TOKT_MACRO      = 'macro'
    TOKT_PUBLIC     = 'public'
    TOKT_PROTECTED  = 'protected'
    TOKT_PRIVATE    = 'private'
    TOKT_STATIC     = 'static'
    TOKT_FINAL      = 'final'
    TOKT_IMPORT     = 'import'
    TOKT_RETURN     = 'return'
    TOKT_ID         = 'identifier'
    TOKT_DOT        = 'dot'
    TOKT_COMMA      = 'comma'
    TOKT_SEMICOLON  = 'semicolon'
    TOKT_DEF        = 'definer'
    TOKT_LCBRACK    = 'left curly bracket'
    TOKT_RCBRACK    = 'right curly bracket'
    TOKT_LPAREN     = 'left parenthesis'
    TOKT_RPAREN     = 'right parenthesis'
    TOKT_INT        = 'integer'
    TOKT_FLOAT      = 'float'
    TOKT_STRING     = 'string'
    TOKT_PLUS       = 'plus'
    TOKT_MINUS      = 'minus'
    TOKT_MULT       = 'multiplication'
    TOKT_DIV        = 'division'
    TOKT_POW        = 'power'
    TOKT_CEXPR      = 'c expression'
    TOKT_EOF        = 'end of file'

    def __init__(self, type_, start, end=None, value=None):
        self.type   = type_
        self.start  = start
        self.end    = end if end else start
        self.value  = value
    
    def __repr__(self):
        return f'[{self.type}: {self.value}]' if self.value else f'[{self.type}]'
    
    def is_type(self, type_): return self.type == type_
