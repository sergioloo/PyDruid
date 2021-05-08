from text import Token


class Initializer:
    VB_PUBLIC       = 'public'
    VB_PROTECTED    = 'protected'
    VB_PRIVATE      = 'private'

    def __init__(self, id_, type_, visibility=VB_PROTECTED, static=False, final=False):
        self.id         : str   = id_
        self.visibility : str   = visibility
        self.static     : bool  = static
        self.final      : bool  = final
        self.type       : str   = type_
