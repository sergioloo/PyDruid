class Statement:
    ST_UNDEFINED    = 'undefined'
    ST_FACTOR       = 'factor'
    ST_BIN_OP       = 'binary operation'
    ST_RETURN       = 'return'

    def __init__(self, type_=None, parent=None):
        self.parent = parent
        self.indent = parent.indent + 1 if parent else 0
        self.type   = type_ if type_ else self.ST_UNDEFINED
    
    def to_c(self): pass
