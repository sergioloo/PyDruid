class Initializer:
    VB_PUBLIC       = 'public'
    VB_PROTECTED    = 'protected'
    VB_PRIVATE      = 'private'

    ST_CLASS        = 'class'

    def __init__(self, id_, vb, static, final, type_):
        self.id         = id_
        self.visibility = vb
        self.static     = static
        self.final      = final
        self.type       = type_
