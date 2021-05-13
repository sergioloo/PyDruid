from utils.error import Error


class ScopeNode:
    def __init__(self, id_, parent=None):
        self.id     = id_
        self.scope  = {}
        self.parent = parent

        if parent: parent.register_raw(self)
    
    def __getitem__(self, id_):
        return self.scope.get(id_)
    
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

    def get_id(self, id_):
        if not self[id_]:
            if self.parent: return self.parent.get_id(id_)
            else:           Error(f"'{id_}' was not declared in this scope.")

        parent = self
        result = id_

        while parent:
            result = f'{parent.id}_{result}'
            parent = parent.parent
        
        return result        
