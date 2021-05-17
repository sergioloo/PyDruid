from .node import Node


class Symbol(Node):
    VB_PUBLIC       = 'public'
    VB_PROTECTED    = 'protected'
    VB_PRIVATE      = 'private'

    TM_PROTOTYPE    = 'prototype'
    TM_DEFINITION   = 'definition'

    def __init__(self, **kwargs):
        Node.__init__(self, **kwargs)

        self.id         = kwargs['id']          if 'id'         in kwargs else ''

        self.visibility = kwargs['visibility']  if 'visibility' in kwargs else self.VB_PROTECTED
        self.static     = kwargs['static']      if 'static'     in kwargs else False
        self.final      = kwargs['final']       if 'final'      in kwargs else False
    
    def to_string(self, mode):
        pass
    
    def get_full_id(self) -> str:
        result = self.id

        parent = self.parent
        while parent and isinstance(parent, Symbol):
            result = f'{parent.id}_{result}'
            parent = parent.parent
        
        return result
