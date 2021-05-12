class ScopeNode:
    def __init__(self, id_):
        self.id     = id_
        self.scope  = {}
    
    def __getitem__(self, id_):
        return self.scope[id_]

    def register(self, id_, n_id):
        self.scope[id_] = ScopeNode(n_id)
        return self.scope[id_]
