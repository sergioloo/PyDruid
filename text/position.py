class Position:
    def __init__(self, idx, ln, col, f, fn):
        self.index  = idx
        self.line   = ln
        self.column = col

        self.char       = None
        self.file       = f
        self.filename   = fn

        self.__update()
    
    def __update(self):
        self.char = self.file[self.index] if self.index < len(self.file) else None

        if self.char == '\n':
            self.line += 1
            self.column = -1
    
    def advance(self):
        self.index  += 1
        self.column += 1
        
        self.__update()

        return self.char
    
    def copy(self):
        return Position(
            self.index, self.line, self.column, self.file, self.filename
        )
