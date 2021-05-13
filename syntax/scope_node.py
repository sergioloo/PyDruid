class ScopeNode:
    def __init__(self, id_, parent=None):
        self.id     = id_
        self.scope  = {}

        if parent: parent.register_raw(self)
    
    def __getitem__(self, id_):
        return self.scope[id_]
    
    def __repr__(self):
        result = f'[({self.id}): '

        for scope in self.scope:
            result += str(self[scope])
        
        return f'{result}]'

    def register(self, id_):
        self.scope[id_] = ScopeNode(id_)
        return self.scope[id_]
    
    def register_raw(self, scope):
        self.scope[scope.id] = scope
