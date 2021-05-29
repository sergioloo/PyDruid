class Accessibility:
    """
    This is not a node. It's an object used in symbols in order to know
    if they can be used from the current scope. If not, an exception will
    be thrown by the compiler.
    """

    VB_PUBLIC       = 'public'
    VB_PROTECTED    = 'protected'
    VB_PRIVATE      = 'private'

    def __init__(self, vb):
        self.accessibility = vb
    
    def __repr__(self) -> str:
        return self.accessibility
    
    @classmethod
    def public(cls): return cls(cls.VB_PUBLIC)
    
    @classmethod
    def protected(cls): return cls(cls.VB_PROTECTED)

    @classmethod
    def private(cls): return cls(cls.VB_PRIVATE)
