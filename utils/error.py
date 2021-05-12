from datetime import datetime


class Error:
    INTERNAL_ERROR  = 'internal error'
    WARNING         = 'warning'
    INFO            = 'info'

    COLOR_RED       = '31'
    COLOR_YELLOW    = '33'
    COLOR_BLUE      = '34'

    EXIT_CODE       = -1
    COLOR           = '31'
    TYPE            = 'error'

    def __init__(self, descr, pos=None, tok=None, throw=True, fatal=True, type_=None, color=None):
        self.description    = descr
        self.position       = pos
        self.token          = tok

        self.fatal          = fatal

        if color: self.COLOR = color
        if type_: self.TYPE  = type_

        if throw: self.throw()
    
    def throw(self):
        moment = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        print(f"\x1b[1m[ \x1b[m{moment} \x1b[1;31merror \x1b[37m]: \x1b[m{self.description}")

        if self.position:
            print(f"\x1b[1mlocated at \x1b[m{self.position.filename} {self.position.line}:{self.position.column}")
            line = self.position.file.split('\n')[self.position.line].replace('\t', '')

            print(f"\t{line}")
            print('\t' + ' ' * (self.position.column - 2) + '\x1b[1;31m~\x1b[m')

        elif self.token:
            start   = self.token.start
            end     = self.token.end

            length  = end.column - start.column

            print(f"\x1b[1mlocated at \x1b[m{start.filename} {start.line}:{start.column}")
            line = start.file.split('\n')[start.line].replace('\t', '')

            print(f"\t{line}")
            print('\t' + ' ' * start.column + '\x1b[1;31m' + '~' * length + '\x1b[m')

        if self.fatal: exit(self.EXIT_CODE)
