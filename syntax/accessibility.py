class Accessibility:
    VB_PUBLIC       = 'public'
    VB_PROTECTED    = 'protected'
    VB_PRIVATE      = 'private'
    
    def __init__(self, val):
        self.value = val
    
    @classmethod
    def public(cls):    return cls(cls.VB_PUBLIC)

    @classmethod
    def protected(cls): return cls(cls.VB_PROTECTED)
    
    @classmethod
    def private(cls):   return cls(cls.VB_PRIVATE)
